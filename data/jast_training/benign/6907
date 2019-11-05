import { Dictionary } from "../../objects/dictionary";
var BaseRequest = /** @class */ (function () {
    function BaseRequest() {
        this.Properties = new Dictionary();
        this.Columns = new Dictionary();
    }
    BaseRequest.prototype.Validate = function () {
        for (var _i = 0, _a = this.Properties.Values; _i < _a.length; _i++) {
            var property = _a[_i];
            property.Validation.Clear();
        }
        this.Validation();
        for (var _b = 0, _c = this.Properties.Values; _b < _c.length; _b++) {
            var property = _c[_b];
            property.DefaultValidation();
        }
        for (var _d = 0, _e = this.Properties.Values; _d < _e.length; _d++) {
            var property = _e[_d];
            if (property.Validation.HasValidation)
                return false;
        }
        return true;
    };
    BaseRequest.prototype.Validation = function () { };
    BaseRequest.prototype.ClearProperties = function () {
        for (var _i = 0, _a = this.Properties.Values; _i < _a.length; _i++) {
            var property = _a[_i];
            property.Clear();
            property.Validation.Clear();
        }
    };
    BaseRequest.prototype.ClearValidation = function () {
        for (var _i = 0, _a = this.Properties.Values; _i < _a.length; _i++) {
            var property = _a[_i];
            property.Validation.Clear();
        }
    };
    return BaseRequest;
}());
export { BaseRequest };
