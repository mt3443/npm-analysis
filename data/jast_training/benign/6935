import { DateExtensions } from "../../objects/extensions/date-extensions";
var Validators = /** @class */ (function () {
    function Validators() {
    }
    Validators.IsRequired = function (property) {
        var type = property;
        if (type.HasValue == false) {
            property.Validation.Set("* Required");
            return;
        }
    };
    Validators.IsMinMax = function (property, min, max) {
        var number = property.Item;
        if (Number.isInteger(number)) {
            if (min && max && number < min || number > max)
                property.Validation.Set(property.Label.Name + " must be between " + min + " and " + max + ".");
            else if (min && number < min)
                property.Validation.Set(property.Label.Name + " must be greater than or equal to " + min + ".");
            else if (max && number > max)
                property.Validation.Set(property.Label.Name + " must be less than or equal to " + max + ".");
        }
    };
    Validators.IsDateBeforeAfter = function (beforeProperty, afterProperty, format) {
        var before = DateExtensions.GetDate(beforeProperty.Item, format);
        var after = DateExtensions.GetDate(afterProperty.Item, format);
        if (before && after && before > after)
            beforeProperty.Validation.Set("The " + afterProperty.Label.Name + " cannot be before the " + beforeProperty.Label.Name + ".");
    };
    Validators.IsDateRangeBeforeAfter = function (property, format) {
        var before = DateExtensions.GetDate(property.Item.Start, format);
        var after = DateExtensions.GetDate(property.Item.Finish, format);
        if (before && after && before > after)
            property.Validation.Set("The finish date cannot be before the start date.");
    };
    return Validators;
}());
export { Validators };
