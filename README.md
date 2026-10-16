# Electrochemical Battery Parameters

**面向 DFN/P2D、SPM、SPMe 的可追溯电化学参数与实验数据项目。**

当前版本 **v0.1.0** 包含 LFP／石墨电极 OCP，以及与全电池实验关联的 LG M50 电化学模型参数：查询、比较、插值、数据下载与来源追溯。项目目前为私有 GitHub 仓库；浏览器页面默认只在本机提供，没有配置公开发布。

## 当前数据

| 数据 | 数量 | 说明 |
|---|---:|---|
| SINTEF LFP 低倍率伪 OCP 分支 | 4 | 2 个半电池样品 × 第 3 循环的嵌锂／脱锂分支 |
| SINTEF 石墨低倍率伪 OCP 分支 | 4 | 2 个半电池样品 × 第 3 循环的嵌锂／脱锂分支 |
| Afshar2017 LFP 公式 | 1 | 转录自固定版本 PyBaMM 的公式实现 |
| Chen2020 LG M50 负极公式 | 1 | 上游标作 graphite；原电芯负极包含 graphite/SiOx |

OCP 共 **10 条记录、4 个实测半电池样品**。另外包含 **38 项非 OCP 参数**（36 项标量、2 个交换电流密度函数）和 **3 只 LG M50 全电池的测试文件**。数据来源覆盖 3 项研究：Afshar、Chen、SINTEF；Chen 的论文和配套数据作为不同来源记录，仍属于同一研究。代码分发来源为 PyBaMM。重复样品和两个方向不计为新的研究。

LG M50 资料包包括电极／隔膜厚度、孔隙率、活性材料体积分数、颗粒半径、固相扩散系数、最大浓度、电导率、热参数、初始浓度、容量及电压边界。数值转录自固定版本 PyBaMM 实现，**未声称全部为同一样品的直接实测值**；初始状态和运行边界单独分类。

全电池文件来自 Chen2020 配套公开数据，包含 C/10、C/2、1C、1.5C 的测试及电芯／环境温度。参数与实验按 **同型号、同研究** 关联，未建立同一拆解样品或同批次关联。网页的“电芯与参数”区域可查询、查看实测放电曲线并下载原始或标准化 CSV。

> PyBaMM `Prada2013` 参数集中的 LFP OCP 来自 Afshar2017，石墨 OCP 来自 Chen2020。数据库按单条函数记录来源，不将它们归为 Prada 的 OCP 测量。

## 安装与运行

需要 Python 3.10+；建议 Python 3.12。系统的旧版 `python3` 不适用时，请指定较新的 Python 路径。

```bash
git clone https://github.com/FrankSuperG/electrochemical-battery-parameters.git
cd electrochemical-battery-parameters
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
ebp validate
ebp serve
```

打开 <http://127.0.0.1:8765>：按材料、方向、形式及关键词筛选，勾选曲线比较，点击记录查看来源、实验、限制和下载。页面不加载外部 CDN、分析脚本或远程字体。它支持离线生成；数据读取与曲线求值不联网。

`ebp serve` 绑定 `127.0.0.1`，不自动上传、不启动 GitHub Pages。`ebp build-site --output site` 只生成本地静态文件。请按私有数据的要求管理生成目录及下载文件。

## Python 接口

```python
from ebp import Catalog

catalog = Catalog()
records = catalog.search(material="LFP", representation="table")
curve = catalog.get("lfp-afshar2017-formula")
print(curve(0.5))                   # V vs Li/Li+
x, voltage = curve.sample(501)      # 公式生成的数值采样，不是实测点

measured = records[0]
x_native, v_native = measured.points()
voltage = measured([0.1, 0.5], method="pchip")
measured.export_csv("measured.csv") # 默认保留全部提取点及原始行号等字段
```

线性插值为默认，另支持 PCHIP。所有数值调用拒绝非有限输入及定义域之外的输入，默认不外推。表达式由有限的 AST 解释器计算，不使用 `eval`，不加载任意 Python 参数函数。

```bash
ebp search --material LFP
ebp search sintef --direction lithiation --json
ebp show lfp-afshar2017-formula
ebp export lfp-afshar2017-formula --output formula.csv
ebp export sintef-lfp-d07eb6-c3-lithiation --output metadata.json --format json
```

JSON 导出包括记录、文献、实验和上游文件校验信息。公式 CSV 默认为 401 点生成采样，可用 `--count` 调整；网页的公式 CSV 为 2001 点采样。表格 CSV 默认包含所有保留点；指定 `--count` 才会重采样。

## 非 OCP 参数与关联实验

```python
from ebp import Catalog

catalog = Catalog()
diffusivity = catalog.search_parameters("Negative particle diffusivity")[0]
print(diffusivity.value, diffusivity.record["unit"])

kinetics = catalog.get_parameter("lgm50-negative-exchange-current-density")
print(kinetics(c_e=1000, c_s_surf=10000, c_s_max=30000, T=298.15))

tests = catalog.linked_tests("lg-m50")
rows = catalog.full_cell_data(tests[0]["id"])  # 原始表格字段；电流仍为幅值 + 模式
```

```bash
ebp parameters --cell lg-m50
ebp parameters diffusivity
ebp parameters --category kinetics --json
ebp tests --cell lg-m50
```

原始 Maccor CSV 的 `Current [A]` 为幅值，方向由 `Md=C/D` 表示；标准化文件
`current_charge_positive_A` 显式采用充电正、放电负。传入默认以放电为正的模型接口时需转换符号。
标准化温度为 K；原始文件原样保留，未平滑或重采样。模型初始条件仍需按具体测试设置。

## PyBaMM OCP 组件接口

```bash
python -m pip install -e '.[pybamm]'
PYBAMM_DISABLE_TELEMETRY=true python examples/pybamm_ocp.py
```

`curve.to_pybamm()` 返回 OCP 函数，使用线性 `pybamm.Interpolant` 且关闭外推。公式在转换时生成数值采样，可控制采样数量；它不是完整参数集。

实测曲线只有相对分支容量轴。导入时必须显式提供 `StoichiometryMapping(theta_start, theta_end, evidence)`，表示分支起止点的化学计量比和依据。数据库没有为这 8 条记录提供绝对配平，不应随意填入 0 和 1。映射后仍为有限电流伪 OCP。

## 科学边界

- **电极 OCP、全电池 OCV、带载端电压分别处理。** 当前曲线是相对 Li/Li⁺ 的电极数据。
- **化学计量比 θ、相对通过容量、全电池 SOC 分开。** 每条记录明确坐标含义，页面对不同坐标、材料和方向分组绘图。
- **实测分支不是已证明的平衡曲线。** SINTEF 数据为 C/50 伪 OCP，包含有限电流极化。第三循环统一选取，不按拟合效果挑选。
- **室温不补写为 25°C。** 来源未给出数值温度时保留 `null`。
- **材料数据不自动归属商业电芯。** LG M50 仅与 Chen 公式建立型号级关联；实验室半电池没有商业电芯映射。
- **当前是部分参数集合，没有独立全电池模型验证。** 已关联真实全电池数据；尚未复现 DFN/SPM/SPMe 的预测误差。OCP 组件测试通过不等于全电池预测准确。

详见 [数据规范](docs/DATA_MODEL.md)、[整理方法与来源审计](docs/CURATION.md)、[路线图](docs/ROADMAP.md) 和 [贡献指南](CONTRIBUTING.md)。

## 目录

```text
src/ebp/data/          # 唯一权威数据源，也随 Python 安装包分发
  catalog.json        # 参数记录、表示形式与逐条证据
  curves/             # 所有保留的实测提取点
  sources.json        # 科学来源与代码来源
  experiments.json    # 协议、样品与选取规则
  materials.json      # 材料／电极
  cells.json          # 有证据支持的商业型号关联
  assets.json         # 原始文件 URL、版本与哈希
  parameters.json     # 非 OCP 标量与多变量函数
  full_cell_tests.json# 全电池测试与参数的关联证据
  full_cell/          # 原始和标准化全电池 CSV
  schema/             # JSON Schema
src/ebp/web/          # 静态浏览页面源代码
src/ebp/licenses/     # 随包分发的第三方许可文本
scripts/seed_v01.py   # 从固定原始文件复现种子数据
tests/               # 数据、插值、公式、导出和适配验证
```

原始 Parquet 约 12 MB，保存在被 Git 忽略的 `.cache/upstream/`。仓库分发约 10 MB 的完整提取 CSV，包含 `source_row`、原始电压、电流、容量和测试时间。源码规范及数据同时版本管理；目前不引入在线数据库服务。

## 复现与检查

```bash
python -m pip install -e '.[dev,pybamm]'
python scripts/seed_v01.py --download
ebp validate
PYBAMM_DISABLE_TELEMETRY=true python -m pytest -q
ebp build-site
python -m build
```

复现脚本校验来源发布的 MD5 和记录的 SHA-256。未经用户许可或贡献审查，不自动从其他论文抓取或推断缺失参数。精确依赖快照见 `requirements-lock-py312.txt`；它记录本次 Python 3.12 验证环境，不是其他平台和 Python 版本的通用锁文件。

## 引用与许可

请引用实际使用记录的科学来源，并在采用上游公式代码时保留软件归属。`sources.json` 和每条记录的 JSON 下载均包含出处；[CITATION.cff](CITATION.cff) 描述本项目。

- SINTEF 数据：[Zenodo v3 / DOI 10.5281/zenodo.20086298](https://zenodo.org/records/20086298)，**CC BY 4.0**。
- LG M50 全电池测试：[Chen2020 配套数据 / DOI 10.5281/zenodo.4032561](https://zenodo.org/records/4032561)，**CC BY 4.0**。
- LFP 公式科学归属：[Afshar et al., 2017](https://arxiv.org/abs/1709.03970v1)。
- 石墨公式科学归属：[Chen et al., 2020](https://doi.org/10.1149/1945-7111/ab9050)。
- 公式代码分发：[PyBaMM v25.4.2](https://github.com/pybamm-team/PyBaMM/blob/v25.4.2/src/pybamm/input/parameters/lithium_ion/Prada2013.py)，**BSD-3-Clause**。

原始项目代码和文档使用 MIT；数据及上游公式保留各自许可。完整说明见 [DATA_LICENSES.md](DATA_LICENSES.md)。
