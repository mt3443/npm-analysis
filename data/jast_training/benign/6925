import { Orientation } from '../../../objects/enums/orientation';
import { Validation } from '../../../objects/validation/validation';
var Property = /** @class */ (function () {
    function Property(Label, orientation, IsHidden, IsDisabled) {
        this.Label = Label;
        this.IsHidden = IsHidden;
        this.IsDisabled = IsDisabled;
        this.Validation = new Validation();
        if (orientation)
            this.Orientation = orientation;
        else
            this.Orientation = Orientation.Vertical;
    }
    Object.defineProperty(Property.prototype, "Type", {
        get: function () {
            if (this.IsCheckBox)
                return "CheckBox";
            if (this.IsComboBox)
                return "ComboBox";
            if (this.IsCheckBoxComboBox)
                return "CheckBoxComboBox";
            if (this.IsDatePicker)
                return "DatePicker";
            if (this.IsDateRangePicker)
                return "DateRangePicker";
            if (this.IsMultiSelectTextBox)
                return "MultiSelectTextBox";
            if (this.IsNumericBox)
                return "NumericBox";
            if (this.IsTextarea)
                return "TextArea";
            if (this.IsTextBox)
                return "TextBox";
            if (this.IsRadioGroup)
                return "RadioButton";
            if (this.IsTemplate)
                return "Template";
            return "";
        },
        enumerable: true,
        configurable: true
    });
    Property.prototype.Clear = function () { };
    Property.prototype.DefaultValidation = function () { };
    return Property;
}());
export { Property };
