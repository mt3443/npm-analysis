import * as _ from 'lodash';
export var WebApiTimeUnit;
(function (WebApiTimeUnit) {
    WebApiTimeUnit[WebApiTimeUnit["Day"] = 0] = "Day";
    WebApiTimeUnit[WebApiTimeUnit["Month"] = 1] = "Month";
    WebApiTimeUnit[WebApiTimeUnit["Quarter"] = 2] = "Quarter";
    WebApiTimeUnit[WebApiTimeUnit["Year"] = 3] = "Year";
})(WebApiTimeUnit || (WebApiTimeUnit = {}));
;
var TimeSeriesItem = /** @class */ (function () {
    function TimeSeriesItem(date, value) {
        this.Value = 0;
        this.Date = date;
        if (value !== undefined)
            this.Value = value;
    }
    return TimeSeriesItem;
}());
export { TimeSeriesItem };
var TimeSeries = /** @class */ (function () {
    function TimeSeries(name, data) {
        this.name = name;
        this.Data = data;
        if (!this.Data)
            this.Data = new Array();
    }
    TimeSeries.fromArray = function (series, sortArray, sortDescending) {
        if (sortArray === void 0) { sortArray = true; }
        if (sortDescending === void 0) { sortDescending = false; }
        if (!sortArray)
            series = series;
        else
            series = _(series).orderBy(function (item) { return item.Date; }, [sortDescending ? "desc" : "asc"]).value();
        return new TimeSeries(null, series);
    };
    TimeSeries.prototype.addItem = function (date, value) {
        this.Data.push(new TimeSeriesItem(date, value));
    };
    TimeSeries.prototype.sumByTimePeriod = function (startDate, duration, durationUnit) {
        var endDate = null;
        if (duration) {
            endDate = new Date(durationUnit == WebApiTimeUnit.Year ? startDate.getFullYear() + duration : startDate.getFullYear(), durationUnit == WebApiTimeUnit.Month ? startDate.getMonth() + duration : startDate.getMonth(), durationUnit == WebApiTimeUnit.Day ? startDate.getDate() + duration : startDate.getDate());
        }
        return _(this.Data).filter(function (d) { return d.Date.getTime() >= startDate.getTime() && (!endDate || d.Date.getTime() < endDate.getTime()); }).sumBy(function (d) { return d.Value; });
    };
    TimeSeries.prototype.valueAtDate = function (date) {
        if (!this.Data || this.Data.length == 0)
            return null;
        var retVal = _(this.Data).filter(function (d) { return d.Date.getTime() <= date.getTime(); })
            .last();
        return retVal ? retVal.Value : null;
    };
    TimeSeries.prototype.valueAtEndDuration = function (startDate, duration, durationUnit) {
        if (!this.Data || this.Data.length == 0)
            return null;
        var endDate = new Date(durationUnit == WebApiTimeUnit.Year ? startDate.getFullYear() + duration : startDate.getFullYear(), durationUnit == WebApiTimeUnit.Month ? startDate.getMonth() + duration : startDate.getMonth(), durationUnit == WebApiTimeUnit.Day ? startDate.getDate() + duration : startDate.getDate());
        var retVal = _(this.Data).filter(function (d) { return d.Date.getTime() < endDate.getTime(); })
            .last();
        return retVal ? retVal.Value : null;
    };
    /// <summary>
    /// Converts an absolute time series to a delta time series (ie one whose values represent *changes* in quantity instead of absolute quantities)
    /// </summary>
    /// <param name="series">The series.</param>
    /// <returns>TimeSeries.</returns>
    TimeSeries.AbsoluteToDeltaSeries = function (series) {
        var current = 0;
        var n = 0;
        var tmp = new Array(series.Data.length);
        _(series.Data).orderBy(function (d) { return d.Date; })
            .forEach(function (item) {
            tmp[n++] = new TimeSeriesItem(item.Date, item.Value - current);
            current = item.Value;
        });
        return tmp;
    };
    /// <summary>
    /// For absolute time series, multiple consecutive dates with the same values are redundant.  This
    /// method returns a new time series with these items filtered out.
    /// </summary>
    /// <param name="series"></param>
    /// <returns></returns>
    TimeSeries.FilterRedundant = function (series) {
        var tmp = new Array();
        var lastValue = 0;
        _(series.Data).orderBy(function (d) { return d.Date; })
            .forEach(function (item) {
            if (item.Value != lastValue) {
                tmp.push(item);
                lastValue = item.Value;
            }
        });
        return TimeSeries.fromArray(tmp);
    };
    /// Creates a new time series that is the sum of a collection of time series
    TimeSeries.AddMerge = function (timeseries) {
        var currentDate;
        var currentValue = 0;
        var tmp = new Array();
        _(timeseries).map(TimeSeries.AbsoluteToDeltaSeries)
            .flatten()
            .orderBy(function (item) { return item.Date; })
            .forEach(function (item) {
            // On the first item, set the 'currentDate'
            if (!currentDate)
                currentDate = item.Date;
            // If the date has changed, add the time series item (based on the current totals from merging the delta series)
            if (currentDate.getTime() != item.Date.getTime()) {
                // Only create a new time series item if the value has changed
                tmp.push(new TimeSeriesItem(currentDate, currentValue));
                currentDate = item.Date;
            }
            // Add up the delta values
            currentValue += item.Value;
        });
        // If there were any items, add the last item (since it should be contained in currentDate & currentValue, and hasn't been added yet)
        if (currentDate)
            tmp.push(new TimeSeriesItem(currentDate, currentValue));
        return TimeSeries.fromArray(tmp);
    };
    return TimeSeries;
}());
export { TimeSeries };
