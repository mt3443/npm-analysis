var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ChangeDetectionStrategy, ChangeDetectorRef, ViewContainerRef, forwardRef, EventEmitter, Input, Output } from '@angular/core';
import { NG_VALUE_ACCESSOR } from '@angular/forms';
import * as moment_ from 'moment';
var moment = moment_.default || moment_;
export var CALENDAR_VALUE_ACCESSOR = {
    provide: NG_VALUE_ACCESSOR,
    useExisting: forwardRef(function () { return DatePickerComponent; }),
    multi: true
};
var DatePickerComponent = /** @class */ (function () {
    function DatePickerComponent(changeDetectorRef, viewContainerRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.ValueChange = new EventEmitter();
        this.TextChange = new EventEmitter();
        this.date = moment();
        this.days = [];
        this.onTouchedCallback = function () { };
        this.changeDetectorRef.detach();
        this.el = viewContainerRef.element.nativeElement;
        this.clickEvent = this.HandleClick.bind(this);
    }
    Object.defineProperty(DatePickerComponent.prototype, "IsDropDownOpen", {
        get: function () {
            return this.isDropDownOpen;
        },
        set: function (value) {
            this.isDropDownOpen = value;
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(DatePickerComponent.prototype, "Text", {
        get: function () {
            return this.text;
        },
        set: function (value) {
            this.text = value;
            this.TextChange.emit(value);
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    DatePickerComponent.prototype.SetValue = function (value) {
        var date = (value instanceof moment) ? value : moment(value, this.Format);
        this.Value = date.format(this.Format);
        this.ValueChange.emit(this.Value);
        this.Text = this.Value;
    };
    DatePickerComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.IsDropDownOpen = this.IsDropDownOpen || false;
        this.Format = this.Format || 'DD-MMM-YYYY';
        this.TooltipContent = "Date format is " + this.Format;
        this.firstWeekdaySunday = this.firstWeekdaySunday || false;
        setTimeout(function () {
            if (_this.Value) {
                //   let value = moment();
                _this.Text = _this.Value;
                _this.changeDetectorRef.detectChanges();
            }
            _this.generateCalendar();
        });
        var body = document.querySelector('body');
        body.addEventListener('click', this.clickEvent, false);
        this.changeDetectorRef.detectChanges();
    };
    DatePickerComponent.prototype.ngOnDestroy = function () {
        var body = document.querySelector('body');
        body.removeEventListener('click', this.clickEvent, false);
    };
    DatePickerComponent.prototype.HandleClick = function (e) {
        if (!this.IsDropDownOpen || !e.target) {
            return;
        }
        ;
        if (this.el !== e.target && !this.el.contains(e.target)) {
            this.close();
        }
    };
    DatePickerComponent.prototype.onTextChange = function (newValue) {
        var date = moment(newValue, this.Format, true);
        if (date.isValid()) {
            this.Value = date.format(this.Format);
            this.ValueChange.emit(this.Value);
            this.date = date;
            this.ShowTooltip = false;
            this.generateCalendar();
        }
        else {
            this.Value = undefined;
            this.ShowTooltip = true;
        }
        this.Text = newValue;
        this.ValueChange.emit(this.Value);
    };
    DatePickerComponent.prototype.onBlurChange = function (value) {
        this.ShowTooltip = false;
    };
    DatePickerComponent.prototype.onFocusChange = function (value) {
        if (this.Value == undefined)
            this.ShowTooltip = true;
    };
    DatePickerComponent.prototype.generateCalendar = function () {
        var date = moment(this.date);
        var month = date.month();
        var year = date.year();
        var n = 1;
        var firstWeekDay = (this.firstWeekdaySunday) ? date.date(2).day() : date.date(1).day();
        if (firstWeekDay !== 1) {
            n -= (firstWeekDay + 6) % 7;
        }
        this.days = [];
        var selectedDate = moment(this.Value, this.Format);
        for (var i = n; i <= date.endOf('month').date(); i += 1) {
            var currentDate = moment(i + "." + (month + 1) + "." + year, 'DD.MM.YYYY');
            var today = (moment().isSame(currentDate, 'day') && moment().isSame(currentDate, 'month')) ? true : false;
            var selected = (selectedDate.isSame(currentDate, 'day')) ? true : false;
            if (i > 0) {
                this.days.push({
                    day: i,
                    month: month + 1,
                    year: year,
                    enabled: true,
                    today: today,
                    selected: selected
                });
            }
            else {
                this.days.push({
                    day: null,
                    month: null,
                    year: null,
                    enabled: false,
                    today: false,
                    selected: false
                });
            }
        }
        this.weeks = [];
        var chunkSize = 7;
        for (var i = 0; i < this.days.length; i += chunkSize)
            this.weeks.push(this.days.slice(i, i + chunkSize));
    };
    DatePickerComponent.prototype.selectDate = function (e, d) {
        e.preventDefault();
        var date = d;
        var selectedDate = moment(date.day + "." + date.month + "." + date.year, 'DD.MM.YYYY');
        this.SetValue(selectedDate);
        this.close();
        this.generateCalendar();
    };
    DatePickerComponent.prototype.prevMonth = function () {
        this.date = this.date.subtract(1, 'month');
        this.generateCalendar();
        this.changeDetectorRef.detectChanges();
    };
    DatePickerComponent.prototype.nextMonth = function () {
        this.date = this.date.add(1, 'month');
        this.generateCalendar();
        this.changeDetectorRef.detectChanges();
    };
    DatePickerComponent.prototype.writeValue = function (value) {
        this.Value = value;
    };
    DatePickerComponent.prototype.registerOnChange = function (fn) {
        this.ValueChange = fn;
    };
    DatePickerComponent.prototype.registerOnTouched = function (fn) {
        this.onTouchedCallback = fn;
    };
    DatePickerComponent.prototype.open = function () {
        this.IsDropDownOpen = true;
    };
    DatePickerComponent.prototype.close = function () {
        this.IsDropDownOpen = false;
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], DatePickerComponent.prototype, "Format", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], DatePickerComponent.prototype, "firstWeekdaySunday", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], DatePickerComponent.prototype, "ShowTooltip", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], DatePickerComponent.prototype, "TooltipContent", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], DatePickerComponent.prototype, "Label", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], DatePickerComponent.prototype, "Watermark", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], DatePickerComponent.prototype, "Value", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], DatePickerComponent.prototype, "ValueChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], DatePickerComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], DatePickerComponent.prototype, "IsDateTime", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], DatePickerComponent.prototype, "TextChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean),
        __metadata("design:paramtypes", [Boolean])
    ], DatePickerComponent.prototype, "IsDropDownOpen", null);
    __decorate([
        Input(),
        __metadata("design:type", String),
        __metadata("design:paramtypes", [String])
    ], DatePickerComponent.prototype, "Text", null);
    DatePickerComponent = __decorate([
        Component({
            selector: 'pm-date-picker',
            //templateUrl: './app/controls/components/date-picker/date-picker.html',
            templateUrl: './date-picker.html',
            changeDetection: ChangeDetectionStrategy.OnPush,
            providers: [CALENDAR_VALUE_ACCESSOR]
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            ViewContainerRef])
    ], DatePickerComponent);
    return DatePickerComponent;
}());
export { DatePickerComponent };
