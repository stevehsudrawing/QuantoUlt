# Simple Components

## Option

- `Shape` Meter named `Meter(Any)Background`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalComponentOptionBackground`, Variables required:
        - `[#CURRENTSECTION]WidthFormula`
        - `[#CURRENTSECTION]HeightFormula`
        - `[#CURRENTSECTION]LayerType`

## Rich Tooltip

- `Shape` Meter named `Meter(ParentComponentName)Background`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalComponentOptionBackground`, Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]AdditionalMeterGroupName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]WidthFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]HeightFormula`
- Any type of Meter named `Meter(ParentComponentName)(Any)`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalComponentOptionRichTooltipApplyMeterGroup`, Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `[#CURRENTSECTION]RelativeXFormula`
        - `[#CURRENTSECTION]RelativeYFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]ChildOffsetXFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]ChildOffsetYFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]AdditionalMeterGroupName`

Sample:

```INI
[Variables]
    MeterSampleRichTooltipBackgroundParentComponentName = "SampleRichTooltip"
    ComponentSampleRichTooltipAdditionalMeterGroupName  = "MeterGroupInSampleContainer"
    ComponentSampleRichTooltipWidthFormula              = ((240 + 24))
    ComponentSampleRichTooltipHeightFormula             = (([MeterSampleRichTooltipString:H] + 24))
    ComponentSampleRichTooltipChildOffsetXFormula       = (- [MeterSampleContainer:X])
    ComponentSampleRichTooltipChildOffsetYFormula       = (- [MeterSampleContainer:Y])
    MeterSampleRichTooltipStringParentComponentName     = "SampleRichTooltip"
    MeterSampleRichTooltipStringRelativeXFormula        = (12)
    MeterSampleRichTooltipStringRelativeYFormula        = (12)

[MeterSampleRichTooltipBackground]
    Meter      = Shape
    MeterStyle = StyleGlobal | StyleSkinMetersInSampleContainer | StyleGlobalComponentOptionRichTooltipBackground | StyleGlobalComponentOptionRichTooltipShowUntilMouseLeaves
    X          = ([MeterSampleOption5Control3ButtonFace:XW] - [MeterSampleContainer:X] - #ComponentSampleRichTooltipWidthFormula#)
    Y          = ([MeterSampleOption5Control3ButtonFace:YH] - [MeterSampleContainer:Y] + 4)

[MeterSampleRichTooltipString]
    Meter      = String
    MeterStyle = StyleGlobal | StyleSkinMetersInSampleContainer | StyleGlobalComponentOptionRichTooltipChild | StyleGlobalComponentOptionRichTooltipChildHidden | StyleGlobalString | StyleGlobalDisableForegroundOpacity | StyleGlobalQuantoAdvancedTextFormatsRenderer
    Text       = "++2**Sample**++2#CRLF##CRLF#This is a sample Rich Tooltip."
    W          = (240)
    ClipString = 2
```

## Button

- `Shape` Meter named `Meter(ParentComponentName)Face`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalShapeHover`
    - `StyleGlobalComponentButtonFace` (**Conflict with** `StyleGlobalComponentButtonInvisibleFace`, `StyleGlobalComponentButtonStringInputFace`), Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]WidthFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]HeightFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]LayerType`
        - `Component[#[#CURRENTSECTION]ParentComponentName]LeftMouseClickAction`
        - `Component[#[#CURRENTSECTION]ParentComponentName]RightMouseClickAction`
    - `StyleGlobalComponentButtonInvisibleFace` (**Conflict with** `StyleGlobalComponentButtonFace`, `StyleGlobalComponentButtonStringInputFace`), Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]WidthFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]HeightFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]LeftMouseClickAction`
        - `Component[#[#CURRENTSECTION]ParentComponentName]RightMouseClickAction`
    - `StyleGlobalComponentButtonStringInputFace` (**Conflict with** `StyleGlobalComponentButtonFace`, `StyleGlobalComponentButtonInvisibleFace`), Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]WidthFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]HeightFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]LayerType`
        - `Component[#[#CURRENTSECTION]ParentComponentName]LeftMouseClickAction`
        - `Component[#[#CURRENTSECTION]ParentComponentName]RightMouseClickAction`
    - `StyleGlobalComponentButtonFaceModifyButtonBackgroundToGlobalAccentColorFilling` (Optional)
- `String` Meter (Optional) named `Meter(ParentComponentName)String`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalString`
    - `StyleGlobalDisableForegroundOpacity` (Optional)
    - `StyleGlobalComponentButtonString`, Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]ChildOffsetXFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]ChildOffsetYFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]StringText`
        - `Component[#[#CURRENTSECTION]ParentComponentName]TooltipText`
    - `StyleGlobalComponentButtonStringModifyStringAlignToLeftCenter` (Optional), Variables required:
        - `Component[#[#CURRENTSECTION]ParentComponentName]StringRelativeXOffsetFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]StringShortenWidthFormula`
    - `StyleGlobalComponentButtonDisplayModifyTintColorToAccentForegroundColor` (Optional)
- `Image` Meter (Optional) named `Meter(ParentComponentName)Image`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalMonoImage` (Optional)
    - `StyleGlobalDisableForegroundOpacity` (Optional)
    - `StyleGlobalComponentButtonImage`, Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]ChildOffsetXFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]ChildOffsetYFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]ImageWidthFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]ImageHeightFormula`
        - `Component[#[#CURRENTSECTION]ParentComponentName]ImagePathToFile`
        - `Component[#[#CURRENTSECTION]ParentComponentName]TooltipText`
    - `StyleGlobalComponentButtonImageModifyPositionX` (Optional), Variables required:
        - `Component[#[#CURRENTSECTION]ParentComponentName]ImageRelativeXOffsetFormula`
    - `StyleGlobalComponentButtonDisplayModifyTintColorToAccentForegroundColor` (Optional)
- `Shape` Meter (Optional) named `Meter(ParentComponentName)ActivatedCover`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalComponentButtonActivatedCover`, Variables required:
        - `[#CURRENTSECTION]ParentComponentName`

Sample:

```INI
[Variables]
    MeterSampleButtonFaceParentComponentName   = "SampleButton"
    MeterSampleButtonStringParentComponentName = "SampleButton"
    ComponentSampleButtonChildOffsetXFormula   = (- [MeterSampleContainer:X])
    ComponentSampleButtonChildOffsetYFormula   = (- [MeterSampleContainer:Y])
    ComponentSampleButtonWidthFormula          = (80)
    ComponentSampleButtonHeightFormula         = (32)
    ComponentSampleButtonLeftMouseClickAction  = [!ShowMeterGroup "MeterGroupComponentSampleRichTooltip"] [!Update] [!Redraw]
    ComponentSampleButtonRightMouseClickAction = #NullAction#
    ComponentSampleButtonTooltipText           = #NullString#
    ComponentSampleButtonLayerType             = 1
    ComponentSampleButtonStringText            = "#TextClickMe#"

[MeterSampleButtonFace]
    Meter = Shape
    MeterStyle = StyleGlobal | StyleSkinMetersInSampleContainer | StyleGlobalShapeHover | StyleGlobalComponentButtonFace

[MeterSampleButtonString]
    Meter = String
    MeterStyle = StyleGlobal | StyleSkinMetersInSampleContainer | StyleGlobalString | StyleGlobalDisableForegroundOpacity | StyleGlobalComponentButtonString
```

## Switch

- `Shape` Meter named `Meter(ParentComponentName)Face`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalShapeHover`
    - `StyleGlobalComponentSwitchFaceStatus0` (**Conflict with** `StyleGlobalComponentSwitchFaceStatus1`), Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]Status0LeftMouseClickAction`
    - `StyleGlobalComponentSwitchFaceStatus1` (**Conflict with** `StyleGlobalComponentSwitchFaceStatus0`), Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]Status1LeftMouseClickAction`

Sample:

```INI
[Variables]
    MeterSampleSwitchFaceParentComponentName         = "SampleSwitch"
    ComponentSampleSwitchStatus0LeftMouseClickAction = [!SetVariable "SkinSampleType" " 1"] [!WriteKeyValue "Variables" "SkinSampleType" " 1" "#CurrentSkinSettingsProfilePathToFile#"] [!Update]
    ComponentSampleSwitchStatus1LeftMouseClickAction = [!SetVariable "SkinSampleType" " 0"] [!WriteKeyValue "Variables" "SkinSampleType" " 0" "#CurrentSkinSettingsProfilePathToFile#"] [!Update]

[MeterSampleSwitchFace]
    Meter      = Shape
    MeterStyle = StyleGlobal | StyleSkinMetersInSampleContainer | StyleGlobalShapeHover | StyleGlobalComponentSwitchFaceStatus#SkinSampleType#
```

## Resizing Entry

- `Shape` Meter named `Meter(ParentComponentName)Container`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalComponentResizeEntryContainer`, Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]MouseActionCursorName`
        - `Component[#[#CURRENTSECTION]ParentComponentName]SwitchToConfigFileName`
- `Shape` Meter named `Meter(ParentComponentName)Face`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalShapeHover`
    - `StyleGlobalComponentResizeEntryFace`, Variables required:
        - `[#CURRENTSECTION]ParentComponentName`
- `Image` Meter named `Meter(ParentComponentName)Image`, applying the following Meter Styles:
    - `StyleGlobal`
    - `StyleGlobalMonoImage`
    - `StyleGlobalDisableForegroundOpacity`
    - `StyleGlobalComponentResizeEntryImage`, Variables required:
        - `[#CURRENTSECTION]ParentComponentName`

Sample:

```INI
[Variables]
    MeterSampleResizeEntryContainerParentComponentName = "SampleResizeEntry"
    MeterSampleResizeEntryFaceParentComponentName      = "SampleResizeEntry"
    MeterSampleResizeEntryImageParentComponentName     = "SampleResizeEntry"
    ComponentSampleResizeEntryMouseActionCursorName    = "SIZE_NWSE"
    ComponentSampleResizeEntrySwitchToConfigFileName   = "Resizing.ini"

[MeterSampleResizeEntryContainer]
    Meter      = Shape
    MeterStyle = StyleGlobal | StyleGlobalComponentResizeEntryContainer

[MeterSampleResizeEntryFace]
    Meter      = Shape
    MeterStyle = StyleGlobal | StyleGlobalShapeHover | StyleGlobalComponentResizeEntryFace

[MeterSampleResizeEntryImage]
    Meter      = Image
    MeterStyle = StyleGlobal | StyleGlobalMonoImage | StyleGlobalDisableForegroundOpacity | StyleGlobalComponentResizeEntryImage
```

# Complex Components

For some overly complex components, scripts for automatic generation are provided. To use them, write a `Script` Measure and import a required sub-skin.

## Container Scroll Bar

- Any type of Meter named `Meter(ContainerName)Container`, Options required:
    - `MeterStyle`, **must be** `StyleGlobal | StyleGlobalComponentScrollableContainerWhenLengthEnoughToShowScrollBarTypeIs[MeasureCalcIs(ContainerName)ContentLengthEnoughToShowScrollBar]AndGlobalTouchScreenModeTypeIs#GlobalTouchScreenModeType#`
    - `X`, `Y` and other necessary Options
- A Meter Style named `StyleSkinMetersIn(ContainerName)Container`, Options required:
    - `Container`, **must be** `Meter(ContainerName)Container`
    - `Group`, **must be** `MeterGroupIn(ContainerName)Container`
- `Script` Measure named `MeasureScriptGenerateComponent(ContainerName)ContainerScrollBar`, Options required:
    - `ScriptFile`, **must be** `#@#Scripts\SubSkinGenerator\Components\ContainerScrollBar.lua`
    - `ContainerName`, **must be** `(ContainerName)`
    - `Orientation`, can be `Vertical` or `Horizontal`
    - `PositionOffsetFormula`, example: `([Meter(ContainerName)Container:W] - 16)`
    - `ShortenFormula` (Optional), example: `(16)`
- Additional Variables:
    - `Container(ContainerName)ContentTotalLengthFormula`
    - `Container(ContainerName)ContentPreviousScrolledPixelsValue`, can be `0` or put it in `#CurrentSkinSettingsProfilePathToFile#`
- Import `#Skin@#Temp\(ContainerName)ContainerScrollBar.inc`

```INI
[Variables]
    ContainerSampleContentTotalLengthFormula          = (1024)
    ContainerSampleContentPreviousScrolledPixelsValue = 0

[MeterSampleContainer]
    Meter      = Shape
    MeterStyle = StyleGlobal | StyleGlobalComponentScrollableContainerWhenLengthEnoughToShowScrollBarTypeIs[MeasureCalcIsSampleContentLengthEnoughToShowScrollBar]AndGlobalTouchScreenModeTypeIs#GlobalTouchScreenModeType#
    Shape      = Rectangle 0, 0, (512), (512) | #ShapeDisableStrokeModifierPart#

[StyleSkinMetersInSampleContainer]
    Container = MeterSampleContainer
    Group     = MeterGroupInSampleContainer

; Contents

[MeasureScriptGenerateComponentSampleContainerScrollBar]
    Measure               = Script
    ScriptFile            = #@#Scripts\SubSkinGenerator\Components\ContainerScrollBar.lua
    ContainerName         = Sample
    Orientation           = Vertical
    PositionOffsetFormula = ([MeterSampleContainer:W] - 16)

@include = "#Skin@#Temp\SampleContainerScrollBar.inc"
```
