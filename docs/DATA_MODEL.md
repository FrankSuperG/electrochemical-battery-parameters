# 数据模型 v0.1

权威数据位于 `src/ebp/data/`；JSON 使用 UTF-8，元数据中的未知值为 `null`。
`catalog.json` 受包内 `schema/catalog.schema.json` 约束。参数记录、材料、实验、
电芯、来源和原始文件通过稳定 ID 关联，避免把材料名称当作电芯身份。

## 每条参数记录

| 字段 | 定义 |
|---|---|
| `id` / `version` | 稳定 ID 与记录修订版本 |
| `parameter` | v0.1 为 `electrode_ocp`，为其他物理参数保留扩展路径 |
| `material_id` | 有来源的材料／电极身份 |
| `direction` | 嵌锂、脱锂或未区分；不是全电池充放电的同义词 |
| `measurement` | `pseudo_ocp` 或 `literature_formula` |
| `temperature` / `reference` | 温度状态与 Li/Li⁺ 参比 |
| `x` | 类型、符号、单位、定义域、坐标定义和定义域依据 |
| `y` | 电位定义与 V 单位 |
| `representation` | 离散表格文件、点数、SHA-256，或受限解析表达式 |
| `source_ids` | 多个科学来源与代码分发来源；角色单独描述 |
| `experiment_id` | 具体测试协议与样品；公式可以没有实验记录 |
| `cell_link` | 电芯关联类型与证据；未知关联保持为空 |
| `provenance` | 输入文件、源文件行位置、转换过程与选取参数 |
| `quality` | 逐维记录来源审查、坐标、原始数据、模型和验证状态 |
| `limitations` / `license` | 限制说明与逐条许可 |

## 两种横坐标

- `stoichiometry`：上游函数定义的电极 `theta=c_s/c_s,max`。0–1 是数学区间，
  不暗示已在整个区间完成实验验证。
- `normalized_branch_capacity`：`(Q-Q_first)/(Q_last-Q_first)`，各分支分别归一化。
  嵌锂和脱锂都随测试进程从 0 增至 1；没有反转、配平或假设绝对锂含量。

容量坐标转为化学计量比的线性映射必须显式提供两个端点及证据；不能据归一化
结果自动认定 `theta=0..1`。这也不提供全电池 SOC 映射。

## 表格约定

CSV 至少包含 `x,potential_V`。v0.1 的实测文件还保留 `capacity_Ah,test_time_s,current_A,source_row`。
`source_row` 是原始 Parquet 的零基行位置。`capacity_Ah` 保留上游分支容量原值；
上游列名虽为 `Cumulative Capacity / Ah`，在这些文件中每个半循环重新累计，
因此不会将它解释为全程不重置的 BDF 新版累计吞吐量。

`x` 必须有限且严格递增。相同容量点保留首点，并在 provenance 中记录删除数；
电压保持原值。原始文件完整保存在来源仓库，本项目通过文件哈希锁定。

## 关联和验证

支持 `same_sample`、`same_batch`、`same_model`、`material_only`、`surrogate`。
v0.1 仅使用 `same_model` 和 `material_only`，无商业批次或样品级证据时不补写。

来源文件校验、数值实现测试、OCP 组件适配、完整模型求解、独立实验验证是不同证据。
v0.1 全部记录的 `independent_validation` 为 false。

## 非 OCP 参数和全电池关联

`parameters.json` 保留参数名、单位、类别、标量／多变量函数、来源位置、许可和
限制。类别区分 geometry、electrode、kinetics、thermal、operating_limits、
initial_state，避免把初始条件视为材料常数。函数明确浓度／温度变量、方程
形式和数学定义域；数学定义域不冒充实测有效区间。

`full_cell_tests.json` 保存准确电芯型号、实验样品 ID、来源资产、原始／标准化
文件、关联证据、协议、列结构和处理规则。与参数的 `same_model_same_study`
关联是资料间的证据，不表示同一拆解样品，也不表示本项目已验证模型。

标准化全电池文件用 `current_charge_positive_A` 明示电流约定，温度使用 K，
保留所有观察值及原始行位置。原始 CSV 的 SHA-256 对照上游资产；标准化文件
有独立 SHA-256。两类文件均随包分发，读取不联网。

## 与标准的关系

参数集交换后续对齐 [BPX](https://bpxstandard.com/)，循环测试优先参考
[BDF](https://github.com/battery-data-alliance/battery-data-format)。v0.1 的记录格式
不是 BPX 参数集，也没有将单独 OCP 冒充完整 BPX 文件。历史 BDF 文件按其实际列
含义读取，不因标准更新而静默改变原始语义。GITT、EIS 等不同实验类型后续使用
各自明确的表格结构，不强塞入 OCP 二列表格。
