import * as moment_ from 'moment';
var moment = moment_.default || moment_;
var DateExtensions = /** @class */ (function () {
    function DateExtensions() {
    }
    Object.defineProperty(DateExtensions, "DateToday", {
        get: function () {
            return moment().format('DD-MMM-YYYY');
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DateExtensions, "DateTimeToday", {
        get: function () {
            return moment().format('DD-MMM-YYYY HHmm [Z]');
        },
        enumerable: true,
        configurable: true
    });
    DateExtensions.GetMonthDate = function (value, format) {
        var dateFormat = format || 'MMM-YYYY';
        return moment(value, dateFormat);
    };
    DateExtensions.GetDate = function (value, format) {
        var dateFormat = format || 'DD-MMM-YYYY';
        return moment(value, dateFormat);
    };
    DateExtensions.GetDateTime = function (value, format) {
        var dateFormat = format || 'DD-MMM-YYYY HHmm [Z]';
        return moment(value, dateFormat);
    };
    DateExtensions.GetUtcDate = function (value) {
        return moment(value).utc().format('DD-MMM-YYYY');
    };
    DateExtensions.GetUtcDateTime = function (value) {
        return moment(value).utc().format("DD-MMM-YYYY HHmm [Z]");
    };
    DateExtensions.AddDay = function (value, days, format) {
        var dateFormat = format || 'DD-MMM-YYYY';
        return moment(value, dateFormat).add(days, 'days').format(dateFormat);
    };
    DateExtensions.AddMonth = function (value, months, format) {
        var dateFormat = format || 'DD-MMM-YYYY';
        return moment(value, dateFormat).add(months, 'months').format(dateFormat);
    };
    DateExtensions.AddYear = function (value, years, format) {
        var dateFormat = format || 'DD-MMM-YYYY';
        return moment(value, dateFormat).add(years, 'years').format(dateFormat);
    };
    return DateExtensions;
}());
export { DateExtensions };
