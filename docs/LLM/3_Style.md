### 项目 UI 开发规范总结

本项目采用了 PySide6 和 QSS (Qt 样式表) 实现 Fluent 风格 UI，同时支持深浅色模式切换。UI 开发的核心目标是确保每个界面的控件都符合 **Fluent UI 设计语言**，并能够在不同的显示模式下提供一致且舒适的用户体验。以下是详细的 UI 设计规范及其实现方法，特别是如何通过 QSS 来保障 Fluent 风格与深浅色模式的适配。

---

#### 1. **Fluent 风格设计原则**

Fluent 风格强调现代化、简洁、响应性和一致性的设计，具体表现为：

* **圆角设计**：控件的圆角需要符合现代化设计趋势，通常使用 `border-radius` 设置。
* **简洁的边框和背景**：主要控件如 `QFrame`, `QPushButton`, `QComboBox` 等的边框设计简洁，背景颜色符合品牌色或主题色，避免繁杂的装饰。
* **字体和颜色**：字体颜色、大小、粗细和间距都应遵循设计规范，提供清晰的可读性，同时在不同的模式下适配。
* **hover / active 状态**：控件的 hover 和 active 状态应有明显的视觉反馈，例如背景色变化、边框变化等。

---

#### 2. **深浅色模式切换**

项目要求支持深色模式和浅色模式，并通过 QSS 保证界面在不同模式下能够自动切换样式。使用以下方法来确保深浅色模式适配：

* **颜色方案**：浅色模式使用较明亮的颜色，而深色模式使用较暗的颜色。所有背景、文字、边框、按钮等控件的颜色在两种模式下都应有所不同，以保证用户界面在两种模式下都能清晰易读。
* **QSS 主题切换**：通过设置 `qconfig.theme` 变量，来自动切换浅色与深色模式下的 QSS。通过为 `QFrame`, `QLabel`, `QListView` 等控件定义两套不同的颜色方案，实现不同模式下的界面切换。

---

#### 3. **QSS 设计原则**

使用 QSS 来保证 UI 设计符合 Fluent 风格并支持深浅色模式切换，以下是 QSS 设计的几个核心原则：

* **背景色与边框**：

  * 浅色模式下，背景色为白色或接近白色的浅色，边框通常为浅灰色或与背景色有明显对比的颜色。
  * 深色模式下，背景色为深色或黑色，边框则为深灰色或与背景色对比的较浅的颜色。

* **圆角设计**：所有需要圆角的控件（如 `QFrame`, `QPushButton`, `QComboBox`）需要使用 `border-radius` 来实现流畅的圆角效果。

* **控件的状态反馈**：

  * `QListView`, `QComboBox`, `QPushButton` 等控件在不同状态（如 hover、selected、pressed）时应有显著的变化，通常是背景色的变化或者边框的颜色变化。
  * 选中状态、悬浮状态等需要有视觉上的反馈，避免混淆。

* **字体颜色与大小**：

  * 浅色模式下使用较深的字体颜色（如 `#2e2e2e`），深色模式下使用较亮的字体颜色（如 `#dddddd`），确保良好的可读性。
  * 字体大小和粗细（如 `font-weight: bold`）应当统一，确保与 Fluent 风格的设计一致。

* **统一的控件风格**：

  * **QPushButton**：需要有合适的圆角、背景色、边框以及悬浮、点击时的视觉变化。按钮的文本颜色也应根据深浅色模式适配。
  * **QComboBox**：应有一致的边框样式、圆角，选中项和下拉项的背景色和字体颜色需根据模式进行调整。
  * **QListView**：列表项之间需要有合适的间隔、边框和选中效果，背景色的变化应该与项目的主题色相匹配。

---

#### 4. **具体 QSS 示例：**

以下是 `QComboBox` 和 `QPushButton` 的 QSS 样式代码示例，包含了深浅色模式适配。

**浅色模式 QSS 示例**：

```css
QComboBox {
    background-color: white;
    border: 1px solid #dcdfe6;
    border-radius: 4px;
    padding: 4px 8px;
    color: #2e2e2e;
}

QComboBox:hover {
    border: 1px solid #409eff;
}

QComboBox::drop-down {
    border: none;
    width: 20px;
    subcontrol-origin: padding;
    subcontrol-position: top right;
}

QComboBox QAbstractItemView {
    background-color: white;
    border: 1px solid #dcdfe6;
    selection-background-color: #ecf5ff;
    selection-color: #409eff;
    color: #2e2e2e;
}

QPushButton {
    background-color: #409eff;
    border-radius: 4px;
    color: white;
    font-weight: bold;
    padding: 8px 16px;
}

QPushButton:hover {
    background-color: #66b1ff;
}

QPushButton:pressed {
    background-color: #3384d4;
}
```

**深色模式 QSS 示例**：

```css
QComboBox {
    background-color: #1e1e1e;
    border: 1px solid #444;
    border-radius: 4px;
    padding: 4px 8px;
    color: #dddddd;
}

QComboBox:hover {
    border: 1px solid #70d5f3;
}

QComboBox::drop-down {
    border: none;
    width: 20px;
    subcontrol-origin: padding;
    subcontrol-position: top right;
}

QComboBox QAbstractItemView {
    background-color: #2a2a2a;
    border: 1px solid #444;
    selection-background-color: #3f578f;
    selection-color: white;
    color: #dddddd;
}

QPushButton {
    background-color: #409eff;
    border-radius: 4px;
    color: white;
    font-weight: bold;
    padding: 8px 16px;
}

QPushButton:hover {
    background-color: #66b1ff;
}

QPushButton:pressed {
    background-color: #3384d4;
}
```

---

#### 5. **如何正确设计 UI**

* **控件布局**：合理分配控件的位置与大小，保持界面的平衡和可视性。控件之间的间距应该统一，避免过于拥挤或过于分散。
* **控件颜色与主题匹配**：颜色的选择应当遵循项目主题和设计语言，避免使用不和谐的颜色搭配。
* **交互反馈**：控件的状态变化应清晰可见，用户与界面交互时应能快速察觉到自己的操作是否成功。例如，按钮按下时颜色变化、输入框获得焦点时边框变化等。
* **适配深浅色模式**：在设计时考虑到深色模式和浅色模式的差异，通过 QSS 自动切换，保证用户在不同模式下都有一致的视觉体验。

---

### 总结

通过本项目中的 QSS 规范，能够确保所有界面控件都符合 Fluent 风格，同时能够根据不同的主题（深色模式或浅色模式）进行自适应调整。设计人员应遵循简单、直观且统一的设计原则，避免使用复杂的视觉效果，确保用户界面的可用性和舒适性。在代码实现上，通过细化每个控件的样式，并根据 `qconfig.theme` 设置自动切换不同的样式，从而实现无缝的深浅色模式适配。
