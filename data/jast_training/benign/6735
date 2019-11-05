var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Output, EventEmitter, Component, Input, ElementRef, ViewChild, ChangeDetectionStrategy } from '@angular/core';
import * as d3 from '../../../../bundles/d3-bundle';
import * as Immutable from 'immutable';
import * as _ from 'lodash';
import { Margin } from '../../../objects/margin';
var GraphComponent = /** @class */ (function () {
    function GraphComponent(el) {
        this.el = el;
        this.height = 500;
        this.width = 960;
        this.includeLineDataPoints = true;
        this.includeHoverLine = true;
        this.transitionDuration = 300; // in milliseconds
        this.hideBorder = false;
        this.interpolationMethod = d3.curveLinear;
        this.margin = { top: 0, right: 70, bottom: 100, left: 70 };
        this.xAxisTextRotation = "-45";
        this.AllowZoomX = true;
        this.AllowZoomY = true;
        // includes an area that displays the difference between the first 2 TimeSeries in the linedData.
        this.IncludeDifference = false;
        this.disableWheelZoom = false;
        this.UseContinuousHoverLine = false;
        this.xDomain = null;
        this.yDomain = null;
        this.lineSizePx = "1px";
        this.pointSizeR = 3;
        this.UniqueId = "0"; // unique ID to identify this graph. Necessary for the clip-path URL used for the differences.
        this.TooltipItemChange = new EventEmitter();
        this.isZoomButtonUpdate = false;
    }
    GraphComponent.prototype.ngOnChanges = function (changeDetection) {
        if (changeDetection.lineData !== undefined || changeDetection.pointData !== undefined)
            this.handleDataChange(changeDetection.lineData, changeDetection.pointData);
    };
    GraphComponent.prototype.handleDataChange = function (dataChange, pointChange) {
        var _this = this;
        if ((!dataChange || !dataChange.currentValue) && (!pointChange || !pointChange.currentValue))
            return;
        if (!this.lineData)
            this.lineData = Immutable.List();
        this.mutableData = this.lineData.toArray();
        if (!this.pointData)
            this.pointData = Immutable.List();
        this.mutablePointData = this.pointData.toArray();
        this.mutableDataAxis1 = this.yAxisMutableData();
        this.mutableDataAxis2 = this.yAxis2MutableData();
        if (this.IncludeDifference && this.mutableData.length > 1) {
            var index0 = 0;
            var index1 = 0;
            var list0Done = function () { return index0 == _this.mutableData[0].Data.length; };
            var list1Done = function () { return index1 == _this.mutableData[1].Data.length; };
            this.differenceData = [];
            while (!list0Done() || !list1Done()) {
                if (this.mutableData[0].Data[index0].Date.getTime() < this.mutableData[1].Data[index1].Date.getTime() || list1Done()) {
                    this.differenceData.push({
                        Date: this.mutableData[0].Data[index0].Date,
                        Value0: this.mutableData[0].Data[index0].Value,
                        Value1: index1 == 0 ? 0 : this.mutableData[1].Data[list1Done() ? this.mutableData[1].Data.length - 1 : index1 - 1].Value
                    });
                    index0++;
                }
                else if (this.mutableData[0].Data[index0].Date.getTime() > this.mutableData[1].Data[index1].Date.getTime()) {
                    this.differenceData.push({
                        Date: this.mutableData[1].Data[index1].Date,
                        Value0: index0 == 0 ? 0 : this.mutableData[0].Data[list0Done() ? this.mutableData[0].Data.length - 1 : index0 - 1].Value,
                        Value1: this.mutableData[1].Data[index1].Value
                    });
                    index1++;
                }
                else {
                    this.differenceData.push({
                        Date: this.mutableData[0].Data[index0].Date,
                        Value0: this.mutableData[0].Data[index0].Value,
                        Value1: this.mutableData[1].Data[index1].Value
                    });
                    index1++;
                    index0++;
                }
            }
        }
        this.flattenedItems = [].concat.apply([], this.mutableDataAxis1.map(function (d, idx) { return d.Data.map(function (dd) { return [dd, d.name]; }); }));
        this.flattenedPointItems = [].concat.apply([], this.mutablePointData.map(function (d, idx) { return d.Data.map(function (dd) { return [dd, d.name]; }); }));
        if (this.mutableDataAxis2) {
            this.flattenedItemsAxis2 = [].concat.apply([], this.mutableDataAxis2.map(function (d) { return d.Data.map(function (dd, idx) { return [dd, d.name]; }); }));
        }
        this.drawGraph();
        setTimeout(function () { return _this.zoomPane.call(_this.zoom.transform, d3.zoomIdentity); }, 1);
    };
    GraphComponent.prototype.drawGraph = function () {
        var _this = this;
        if (this.svg) {
            if (this.xDomain) {
                this.x = this.x.domain(this.xDomain);
            }
            else {
                this.x = this.x.domain(d3.extent(_.concat(this.flattenedItems, this.flattenedPointItems), function (d) {
                    return d[0].Date;
                }));
            }
            if (this.yDomain) {
                this.y = this.y.domain(this.yDomain).nice();
            }
            else {
                this.y = this.y.domain([
                    d3.min(_.concat(this.mutableDataAxis1, this.mutablePointData), function (c) { return d3.min(c.Data, function (v) { return v.Value; }); }),
                    d3.max(_.concat(this.mutableDataAxis1, this.mutablePointData), function (c) { return d3.max(c.Data, function (v) { return v.Value; }); })
                ]).nice();
            }
            if (this.mutableDataAxis2) {
                this.y2.domain([
                    d3.min(this.mutableDataAxis2, function (c) { return d3.min(c.Data, function (v) { return v.Value; }); }),
                    d3.max(this.mutableDataAxis2, function (c) { return d3.max(c.Data, function (v) { return v.Value; }); })
                ]).nice();
            }
            d3.zoomIdentity.translate(0, 0).scale(1);
            this.zoomedX = this.x;
            if (this.AllowZoomY) {
                this.zoomedY = this.y;
                this.zoomedY2 = this.y2;
            }
            this.updateAxis(true);
            this.updateGraph();
            //  this.svg.selectAll("*").remove();
            return this.svg;
        }
        this.width = this.width - this.margin.left - this.margin.right;
        this.height = this.height - this.margin.top - this.margin.bottom;
        this.x = d3.scaleTime()
            .range([0, this.width]);
        this.y = d3.scaleLinear()
            .range([this.height, 0]);
        if (this.yAxisSecondAxisDataFilter) {
            this.y2 = d3.scaleLinear()
                .range([this.height, 0]);
            this.y2Axis = d3.axisRight(this.y2);
            this.area = d3.area()
                .x(function (d) { return _this.zoomedX(d.Date); })
                .y1(function (d) { return _this.zoomedY2(d.Value); })
                .y0(function (d) { return _this.zoomedY2(0); })
                .curve(this.interpolationMethod);
        }
        if (this.IncludeDifference) {
            this.differenceArea = d3.area()
                .curve(this.interpolationMethod)
                .x(function (d) {
                return _this.zoomedX(d.Date);
            })
                .y1(function (d) {
                return _this.zoomedY(d.Value0);
            });
        }
        if (this.userColors)
            this.color = d3.scaleOrdinal(this.userColors);
        else
            this.color = d3.scaleOrdinal(["#1f77b4", "#d62728", "#ffba00"]);
        this.xAxis = d3.axisBottom(this.x)
            .tickFormat(function (d) { return _this.multiTimeFormat(d); });
        this.yAxis = d3.axisLeft(this.y);
        this.line = d3.line()
            .x(function (d) { return _this.zoomedX(d.Date); })
            .y(function (d) { return _this.zoomedY(d.Value); })
            .curve(this.interpolationMethod);
        this.svg = d3.select(this.el.nativeElement).append("svg")
            .attr("width", this.width + this.margin.left + this.margin.right)
            .attr("height", this.height + this.margin.top + this.margin.bottom)
            .append("g")
            .attr("transform", "translate(" + this.margin.left + "," + this.margin.top + ")");
        this.svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + this.height + ")");
        this.svg.append("clipPath")
            .attr("id", "clip-" + this.UniqueId)
            .append("rect")
            .attr("x", 0)
            .attr("y", 0)
            .attr("width", this.width)
            .attr("height", this.height);
        this.graphContainer = this.svg.append("g")
            .attr("clip-path", "url(#clip-" + this.UniqueId + ")")
            .append("g");
        if (this.includeHoverLine) {
            this.setupHoverLine();
        }
        this.mutableData = this.lineData.toArray();
        this.mutableDataAxis1 = this.yAxisMutableData();
        this.mutableDataAxis2 = this.yAxis2MutableData();
        this.color.domain(this.mutableData.concat(this.mutablePointData).map(function (d) { return d.name; }));
        this.flattenedItems = [].concat.apply([], this.mutableDataAxis1.map(function (d) { return d.Data.map(function (dd, idx) { return [dd, d.name]; }); }));
        if (this.mutableDataAxis2) {
            this.flattenedItemsAxis2 = [].concat.apply([], this.mutableDataAxis2.map(function (d) { return d.Data.map(function (dd, idx) { return [dd, d.name]; }); }));
            this.y2.domain([
                d3.min(this.mutableDataAxis2, function (c) { return d3.min(c.Data, function (v) { return v.Value; }); }),
                d3.max(this.mutableDataAxis2, function (c) { return d3.max(c.Data, function (v) { return v.Value; }); })
            ]).nice();
        }
        if (this.xDomain) {
            this.x = this.x.domain(this.xDomain);
        }
        else {
            this.x = this.x.domain(d3.extent(_.concat(this.flattenedPointItems, this.flattenedItems), function (d) {
                return d[0].Date;
            }));
        }
        if (this.yDomain) {
            this.y.domain(this.yDomain).nice();
        }
        else {
            this.y.domain([
                d3.min(_.concat(this.mutableDataAxis1, this.mutablePointData), function (c) { return d3.min(c.Data, function (v) { return v.Value; }); }),
                d3.max(_.concat(this.mutableDataAxis1, this.mutablePointData), function (c) { return d3.max(c.Data, function (v) { return v.Value; }); })
            ]).nice();
        }
        this.setupZoomBehavior();
        this.drawBorder();
        this.setupLegend(this.mutableData, this.mutablePointData);
        this.setupZoomButtons();
        this.tooltip = d3.select(this.tooltipElementRef.nativeElement)
            .style("position", "absolute")
            .style("z-index", "10")
            .style("visibility", "hidden");
        this.updateGraph();
        var yAx = this.svg.append("g")
            .attr("class", "y axis");
        var yAx2;
        if (this.yAxisSecondAxisDataFilter) {
            yAx2 = this.svg.append("g")
                .attr("class", "y2 axis")
                .attr("transform", "translate( " + this.width + ", 0 )");
        }
        if (this.yAxisTitle) {
            yAx.append("text")
                .attr("transform", "translate(0," + this.height / 2 + ")rotate(-90)")
                .attr("dx", "4em")
                .attr("dy", "1.31em")
                .style("text-anchor", "end")
                .style("fill", "#000")
                .text(this.yAxisTitle);
        }
        if (this.ySecondAxisTitle) {
            yAx2.append("text")
                .attr("transform", "translate(0," + this.height / 2 + ")rotate(-90)")
                .attr("dx", "4em")
                .attr("dy", "-.31em")
                .style("text-anchor", "end")
                .style("fill", "#000")
                .text(this.ySecondAxisTitle);
        }
    };
    GraphComponent.prototype.multiTimeFormat = function (date) {
        var formatMillisecond = d3.timeFormat("%I:%M:%S.%L"), formatSecond = d3.timeFormat("%I:%M:%S"), formatMinute = d3.timeFormat("%d-%b-%Y %I:%M"), formatHour = d3.timeFormat("%d-%b-%Y %I %p"), formatDay = d3.timeFormat("%d-%b-%Y"), formatWeek = d3.timeFormat("%d-%b-%Y"), formatMonth = d3.timeFormat("%B %Y"), formatYear = d3.timeFormat("%Y");
        return (d3.timeSecond(date) < date ? formatMillisecond
            : d3.timeMinute(date) < date ? formatSecond
                : d3.timeHour(date) < date ? formatMinute
                    : d3.timeDay(date) < date ? formatHour
                        : d3.timeMonth(date) < date ? (d3.timeWeek(date) < date ? formatDay : formatWeek)
                            : d3.timeYear(date) < date ? formatMonth
                                : formatYear)(date);
    };
    GraphComponent.prototype.setupZoomBehavior = function () {
        var _this = this;
        this.zoom = d3.zoom()
            .on("zoom", function () { return _this.zoomUpdate(_this.isZoomButtonUpdate); }); //  .scaleExtent([.5,7]);
        if (this.xExtent) {
            this.zoom.
                translateExtent([[this.x(this.xExtent[0]), 0], [Math.max(this.width, this.x(this.xExtent[1])), Infinity]]);
        }
        if (this.disableWheelZoom)
            this.zoom.filter(function () {
                return !d3.event || (!d3.event.button && !d3.event.wheelDelta);
            });
        this.zoomPane = this.svg.append("rect")
            .attr("class", "zoomPane")
            .attr("width", this.width)
            .attr("height", this.height)
            .call(this.zoom);
    };
    GraphComponent.prototype.setupHoverLine = function () {
        var _this = this;
        var that = this;
        this.hoverLine = this.svg
            .on("mousemove", function (d) { that.updateHoverLine(this); })
            .on("mouseout", function (d) { return _this.removeHoverLine(); })
            .append("g")
            .attr("class", "hoverLine")
            .append("line");
    };
    // filter for the "first" y-axis. Just an inverse of the 2nd filter
    GraphComponent.prototype.yAxisFilter = function (d) {
        return this.yAxisSecondAxisDataFilter ? !this.yAxisSecondAxisDataFilter(d) : true;
    };
    GraphComponent.prototype.yAxisMutableData = function () {
        var _this = this;
        return this.mutableData.filter(function (d) { return _this.yAxisFilter(d); });
    };
    GraphComponent.prototype.yAxis2MutableData = function () {
        var _this = this;
        if (!this.yAxisSecondAxisDataFilter)
            return null;
        return this.mutableData.filter(function (d) { return _this.yAxisSecondAxisDataFilter(d); });
    };
    GraphComponent.prototype.updateHoverLine = function (el) {
        var _this = this;
        var xCoord = d3.mouse(el)[0];
        var vals = this.getValuesAtX(xCoord);
        this.svg.selectAll(".inflated.data-point")
            .attr("r", this.pointSizeR)
            .attr("stroke", undefined)
            .style("stroke-width", undefined)
            .classed("inflated", false);
        var points = this.svg.selectAll(".data-point")
            .filter(function (d) { return vals.values.find(function (v) { return v.value.Date == d[0].Date; }); })
            .attr("r", this.pointSizeR + 2)
            .attr("stroke", "black")
            .style("stroke-width", "1px")
            .classed("inflated", true);
        var selectedDate = vals.values.first().value.Date;
        var hoverX = this.UseContinuousHoverLine ? this.zoomedX(selectedDate) : this.zoomedX(vals.datePos);
        this.hoverLine.attr("y1", 0)
            .attr("y2", this.height)
            .attr("x1", hoverX)
            .attr("x2", hoverX)
            .attr("opacity", 1)
            .style("stroke", "black")
            .style("stroke-width", "1px");
        //  this.tooltip.html(this.hoverLineDisplay(vals));
        var tooltipBounds = this.tooltip.node().getBoundingClientRect();
        // currently, we position the tooltip above the "highest" datapoint, and to the left of the hoverline.
        this.tooltip.style("visibility", "visible")
            .style("top", (_(points.nodes()).map(function (p) { return p.cy.baseVal.value; }).min() - 40) + "px")
            .style("left", function () {
            if (+hoverX > (_this.width / 2))
                return (+hoverX + _this.margin.left - tooltipBounds.width - 15) + "px";
            return (+hoverX + _this.margin.left + 15) + "px";
        });
        this.TooltipItemChange.emit(vals);
    };
    GraphComponent.prototype.removeHoverLine = function () {
        this.tooltip.style("visibility", "hidden");
        this.hoverLine.attr("opacity", 0);
        this.svg.selectAll(".inflated.data-point")
            .attr("r", this.pointSizeR)
            .attr("stroke", undefined)
            .style("stroke-width", undefined)
            .classed("inflated", false);
    };
    GraphComponent.prototype.getValuesAtX = function (xCoord) {
        var curDate = this.zoomedX.invert(xCoord);
        var bisectDate = d3.bisector(function (d) { return d.Date; }).left;
        // line values range from the date of the TimeSeriesItem to the next item in the series.
        var lineValues = this.lineData.map(function (t, i) {
            var curIdx = bisectDate(t.Data, curDate, 1);
            var leftVal = t.Data[curIdx - 1];
            var rightVal = t.Data[curIdx];
            var val;
            if (!leftVal)
                val = rightVal;
            else if (!rightVal)
                val = leftVal;
            else
                val = curDate.getTime() - leftVal.Date.getTime() > rightVal.Date.getTime() - curDate.getTime() ? leftVal : rightVal;
            return { "seriesName": t.name, "value": leftVal };
        });
        var beginningOfDayDate = new Date(curDate.getFullYear(), curDate.getMonth(), curDate.getDate());
        // point values are single point in time.
        var pointValues = this.pointData.map(function (t, i) {
            var item = _(t.Data).filter(function (d) { return d.Date.getTime() == beginningOfDayDate.getTime(); }).first();
            if (!item)
                return undefined;
            return { "seriesName": t.name, "value": item };
        }).filter(function (d) { return d !== undefined; });
        return { "datePos": curDate, "values": lineValues.concat(pointValues) };
    };
    GraphComponent.prototype.drawBorder = function () {
        var strokeOpacity = this.hideBorder ? 0 : 0.9;
        this.svg.append("g")
            .attr("class", "d3 border")
            .append("rect")
            .attr("x", this.margin.left * -1)
            .attr("y", this.margin.top * -1)
            .style("fill", "none")
            .style("stroke", "black")
            .style("stroke-width", "2px")
            .style("stroke-opacity", strokeOpacity)
            .attr("height", this.height + this.margin.top + this.margin.bottom)
            .attr("width", this.width + this.margin.left + this.margin.right);
    };
    GraphComponent.prototype.updateGraph = function () {
        this.updateAxis();
        if (this.IncludeDifference) {
            this.updateDifferenceLines(this.differenceData);
        }
        if (this.yAxisSecondAxisDataFilter)
            this.updateLines(this.mutableDataAxis2, true);
        this.updateLines(this.mutableDataAxis1, false);
        if (this.includeLineDataPoints) {
            if (this.yAxisSecondAxisDataFilter)
                this.updateLinePoints(this.flattenedItemsAxis2, true);
            this.updateLinePoints(this.flattenedItems, false);
        }
        if (this.flattenedPointItems && this.flattenedPointItems.length > 0) {
            this.updateLinePoints(this.flattenedPointItems, false);
        }
    };
    GraphComponent.prototype.zoomUpdate = function (includeTransitions) {
        // if(this.xDomain) {
        //     var tx = d3.zoomIdentity.x,
        //         ty = d3.zoomIdentity.y;
        if (includeTransitions === void 0) { includeTransitions = false; }
        //     tx = Math.min(tx, 0);
        //     tx = Math.max(tx, this.width - this.zoomedX(this.xDomain[1]));
        //     d3.zoomIdentity.translate(tx, ty);
        // }
        this.updateAxis(includeTransitions);
        if (this.IncludeDifference) {
            this.updateExistingDifferenceLines(this.graphContainer.select(".diff-line.diff0"), true, includeTransitions);
            this.updateExistingDifferenceLines(this.graphContainer.select(".diff-line.diff1"), false, includeTransitions);
            this.updateExistingDifference(this.graphContainer.select("clipPath#clip-below-" + this.UniqueId).select("path"), false, includeTransitions);
            this.updateExistingDifference(this.graphContainer.select("clipPath#clip-above-" + this.UniqueId).select("path"), true, includeTransitions);
        }
        if (this.yAxisSecondAxisDataFilter) {
            lines = this.graphContainer.selectAll(".gc-line.ax2");
            this.updateExistingLines(lines, includeTransitions, true);
        }
        var lines = this.graphContainer.selectAll(".gc-line.ax1");
        this.updateExistingLines(lines, includeTransitions, false);
        this.updateExistingLinePoints(this.svg.selectAll(".data-point.ax1"), includeTransitions, false);
        if (this.yAxisSecondAxisDataFilter)
            this.updateExistingLinePoints(this.svg.selectAll(".data-point.ax2"), includeTransitions, true);
        // this.graphContainer.attr("transform","translate("+ (<any>d3.event).translate +")scale(" + d3.event.scale + ")");
    };
    GraphComponent.prototype.setupZoomButtons = function () {
        var _this = this;
        var zoomInButton = d3.select("pm-icon-search-plus")
            .on("click", function () { _this.zoomClick(true); });
        var zoomOutButton = d3.select("pm-icon-search-minus")
            .on("click", function () { _this.zoomClick(false); });
        var resetButton = d3.select("pm-icon-arrows")
            .on("click", function () { _this.zoomClick(false, true); });
    };
    GraphComponent.prototype.zoomClick = function (isZoomIn, isZoomReset) {
        if (isZoomReset === void 0) { isZoomReset = false; }
        var currentDuration = this.transitionDuration;
        this.transitionDuration = currentDuration == 0 ? 500 : currentDuration;
        this.isZoomButtonUpdate = true;
        if (isZoomReset)
            this.zoomPane.call(this.zoom.transform, d3.zoomIdentity);
        else
            this.zoomPane.call(this.zoom.scaleBy, isZoomIn ? 2 : 0.5);
        this.isZoomButtonUpdate = false;
        this.transitionDuration = currentDuration;
    };
    GraphComponent.prototype.setupLegend = function (mutableData, mutablePointData) {
        var _this = this;
        var numberOfLines = mutableData.length;
        var legendContainer = this.svg.append("g");
        var legend = legendContainer
            .attr("font-size", 12)
            .attr("text-anchor", "end")
            .selectAll("g")
            .data(mutableData.concat(mutablePointData))
            .enter().append("g")
            .attr("transform", function (d, i) { return "translate(0," + i * 20 + ")"; });
        legend.filter(function (d, i) { return i < numberOfLines; })
            .append("line")
            .attr("x1", this.width - 19)
            .attr("x2", this.width)
            .attr("y1", 19 / 2)
            .attr("y2", 19 / 2)
            .style('stroke-dasharray', function (d, i) { return i == 0 ? undefined : i * 8 + "," + i * 8; })
            .style("stroke-width", 3)
            .style("stroke", function (d) {
            if (_this.yAxisSecondAxisDataFilter && _this.yAxisSecondAxisDataFilter(d))
                return "lightgray";
            return _this.color(d.name);
        });
        legend.filter(function (d, i) { return i >= numberOfLines; })
            .append("circle")
            .attr("r", 4)
            .attr("cx", this.width - 15)
            .attr("cy", 19 / 2)
            .style("fill", function (d) {
            return _this.color(d.name);
        });
        legend.append("text")
            .attr("x", this.width - 24)
            .attr("y", 9.5)
            .attr("dy", "0.32em")
            .text(function (d) { return d.name; });
        var legendPadding = 5;
        legendContainer.insert("rect", "g")
            .attr("x", legendContainer.node().getBBox().x - legendPadding)
            .attr("y", legendContainer.node().getBBox().y)
            .style("stroke-width", "1")
            .style("stroke", "black")
            .style("fill", "white")
            .style("fill-opacity", 0.8)
            .attr("width", legendContainer.node().getBBox().width + (legendPadding * 2))
            .attr("height", legendContainer.node().getBBox().height + legendPadding);
    };
    GraphComponent.prototype.updateAxis = function (includeTransitions) {
        if (includeTransitions === void 0) { includeTransitions = true; }
        var xAx = this.svg.select(".x.axis");
        if (includeTransitions && this.transitionDuration > 0)
            xAx = xAx.transition()
                .duration(this.transitionDuration);
        if (d3.event != null && d3.event.transform && this.AllowZoomX) {
            this.zoomedX = d3.event.transform.rescaleX(this.x);
        }
        else {
            this.zoomedX = this.zoomedX ? this.zoomedX : this.x;
        }
        var rescaledXAxis = this.xAxis.scale(this.zoomedX);
        xAx.call(rescaledXAxis)
            .selectAll("text")
            .style("text-anchor", "end")
            .attr("dx", "-.3em")
            .attr("dy", ".5em")
            .attr("transform", "rotate(" + this.xAxisTextRotation + ")");
        var yAx = this.svg.select(".y.axis");
        if (includeTransitions && this.transitionDuration > 0)
            yAx = yAx.transition()
                .duration(this.transitionDuration);
        if (d3.event != null && d3.event.transform && this.AllowZoomY) {
            this.zoomedY = d3.event.transform.rescaleY(this.y);
        }
        else {
            this.zoomedY = this.zoomedY ? this.zoomedY : this.y;
        }
        var rescaledYAxis = this.yAxis.scale(this.zoomedY);
        yAx.call(rescaledYAxis);
        if (this.yAxisSecondAxisDataFilter) {
            var yAx2 = this.svg.select(".y2.axis");
            if (includeTransitions && this.transitionDuration > 0)
                yAx2 = yAx2.transition()
                    .duration(this.transitionDuration);
            if (d3.event != null && d3.event.transform && this.AllowZoomY) {
                this.zoomedY2 = d3.event.transform.rescaleY(this.y2);
            }
            else {
                this.zoomedY2 = this.zoomedY2 ? this.zoomedY2 : this.y2;
            }
            var rescaledY2Axis = this.y2Axis.scale(this.zoomedY2);
            yAx2.call(rescaledY2Axis);
        }
    };
    GraphComponent.prototype.updateDifferenceLines = function (differenceData) {
        var y = this.zoomedY;
        var axClass = "ax1";
        var enteredClipsBelow = this.graphContainer.selectAll(".clip-below-" + this.UniqueId).data([differenceData])
            .enter()
            .append("clipPath")
            .attr("id", "clip-below-" + this.UniqueId);
        enteredClipsBelow.append("path")
            .call(this.zoom);
        // enteredClipsBelow.merge(enteredClipsBelow)
        //         .attr("d", d=>this.differenceArea.y0(this.height)(d.Data));
        var enteredClipsAbove = this.graphContainer.selectAll(".clip-above-" + this.UniqueId).data([differenceData])
            .enter()
            .append("clipPath")
            .attr("id", "clip-above-" + this.UniqueId);
        enteredClipsAbove.append("path")
            .call(this.zoom);
        // enteredClipsAbove.merge(enteredClipsAbove)
        this.updateExistingDifference(enteredClipsBelow.merge(enteredClipsBelow).select("path"), false, true);
        this.updateExistingDifference(enteredClipsAbove.merge(enteredClipsAbove).select("path"), true, true);
        // var enteredDiffAbove = this.graphContainer.selectAll(".area.above")
        //     .data([mutableData[0]])
        //         .enter()
        //     .append("path")
        //     .attr("class", "area above")
        //     .attr("clip-path", "url(#clip-above)");
        // enteredDiffAbove.merge(enteredDiffAbove)
        //     .attr("d", d=>this.differenceArea.y0(function (d) { return y(d.Value); })(d.Data));
        // var enteredDiffBelow = this.graphContainer.selectAll(".area.below")
        //     .data([mutableData[1]])
        //         .enter()
        //     .append("path")
        //     .attr("class", "area below")
        //     .attr("clip-path", "url(#clip-below)");
        // enteredDiffBelow.merge(enteredDiffBelow)                
        //     .attr("d", d=> this.differenceArea(d.Data));                
        var line0 = this.graphContainer.selectAll(".diff-line.diff0." + axClass)
            .data([differenceData])
            .enter()
            .append("path")
            .style('opacity', 0)
            .attr("class", "diff-line " + axClass + " diff0")
            .call(this.zoom);
        var line1 = this.graphContainer.selectAll(".diff-line.diff1." + axClass)
            .data([differenceData])
            .enter()
            .append("path")
            .style('opacity', 0)
            .attr("class", "diff-line " + axClass + " diff1")
            .call(this.zoom);
        this.updateExistingDifferenceLines(line0.merge(line0), false, true);
        this.updateExistingDifferenceLines(line1.merge(line1), true, true);
        line0.exit()
            .remove();
        line1.exit()
            .remove();
    };
    GraphComponent.prototype.updateExistingDifferenceLines = function (lines, isAbove, includeTransitions) {
        var _this = this;
        var that = this;
        if (includeTransitions && this.transitionDuration > 0)
            lines = lines.transition().duration(this.transitionDuration);
        lines = lines
            .attr("d", isAbove ? this.differenceArea.y0(function (d) { return _this.zoomedY(d.Value1); }) : this.differenceArea)
            .style('opacity', 1)
            .style("fill", isAbove ? "lightsalmon" : "lightgreen")
            .attr("clip-path", isAbove ? "url(#clip-above-" + this.UniqueId + ")" : "url(#clip-below-" + this.UniqueId + ")");
    };
    GraphComponent.prototype.updateExistingLines = function (lines, includeTransitions, isYAxis2) {
        var _this = this;
        var that = this;
        var shape = isYAxis2 ? this.area : this.line;
        if (includeTransitions && this.transitionDuration > 0) {
            lines = lines.transition().duration(this.transitionDuration);
            if (this.useTweenTransition)
                lines.attrTween("d", function (d) { return that.pathTween(shape(d.Data), 4, this)(); });
            else {
                lines.attr("d", function (d) { return shape(d.Data); });
            }
        }
        else {
            lines.attr("d", function (d) { return shape(d.Data); });
        }
        lines = lines
            .style('opacity', 1)
            .style('stroke-width', this.lineSizePx)
            .style("stroke", function (d) { return _this.color(d.name); });
    };
    GraphComponent.prototype.updateLines = function (mutableData, isYAxis2) {
        var y = isYAxis2 ? this.zoomedY2 : this.zoomedY;
        var axClass = isYAxis2 ? "ax2" : "ax1";
        var gLines = this.graphContainer.selectAll(".chart-line." + axClass)
            .data(mutableData);
        var enteredGLines = gLines.enter()
            .append("g")
            .attr("class", "chart-line " + axClass)
            .call(this.zoom);
        var enteredLines = enteredGLines
            .append("path")
            .style('opacity', 0)
            .style('stroke-dasharray', function (d, i) { return i == 0 ? undefined : i * 8 + "," + i * 8; })
            .attr("class", "gc-line " + axClass);
        this.updateExistingLines(enteredGLines.merge(gLines).select(".gc-line"), true, isYAxis2);
        gLines.exit()
            .remove();
    };
    GraphComponent.prototype.updateExistingDifference = function (clip, isAbove, includeTransitions) {
        if (includeTransitions && this.transitionDuration > 0)
            clip = clip.transition().duration(this.transitionDuration);
        if (isAbove) {
            clip.attr("d", this.differenceArea.y0(0));
        }
        else {
            clip.attr("d", this.differenceArea.y0(this.height));
        }
    };
    GraphComponent.prototype.updateExistingLinePoints = function (circles, includeTransitions, isYAxis2) {
        var _this = this;
        var y = isYAxis2 ? this.zoomedY2 : this.zoomedY;
        if (includeTransitions && this.transitionDuration > 0)
            circles = circles.style('opacity', 1)
                .transition().duration(this.transitionDuration);
        circles.style('opacity', 1)
            .style('fill-opacity', .8)
            .attr("cx", function (d) { return _this.zoomedX(d[0].Date); })
            .attr("cy", function (d) { return y(d[0].Value); });
    };
    GraphComponent.prototype.updateLinePoints = function (dataPoints, isYAxis2) {
        var _this = this;
        var y = isYAxis2 ? this.zoomedY2 : this.zoomedY;
        var axClass = isYAxis2 ? "ax2" : "ax1";
        var circles = this.graphContainer.selectAll(".data-point." + axClass)
            .data(dataPoints, function (d) { return d[0].Date; });
        var enteredCircles = circles.enter().append("circle")
            .attr("r", this.pointSizeR)
            .style("fill", function (d) { return isYAxis2 ? "lightgray" : _this.color(d[1]); })
            .style('opacity', 0)
            .attr("class", "data-point " + axClass)
            .attr("cx", function (d) { return _this.zoomedX(d[0].Date); })
            .attr("cy", function (d) { return y(d[0].Value); })
            .call(this.zoom);
        circles.exit()
            .remove();
        this.updateExistingLinePoints(enteredCircles.merge(circles), true, isYAxis2);
    };
    GraphComponent.prototype.pathTween = function (d1, precision, element) {
        return function () {
            if (!d1)
                return "";
            var path0 = element, path1 = path0.cloneNode(), n0 = path0.getTotalLength(), n1 = (path1.setAttribute("d", d1), path1).getTotalLength();
            // Uniform sampling of distance based on specified precision.
            var distances = [0], i = 0, dt = precision / Math.max(n0, n1);
            while ((i += dt) < 1)
                distances.push(i);
            distances.push(1);
            // Compute point-interpolators at each distance.
            var points = distances.map(function (t) {
                var p0 = path0.getPointAtLength(t * n0), p1 = path1.getPointAtLength(t * n1);
                return d3.interpolate([p0.x, p0.y], [p1.x, p1.y]);
            });
            return function (t) {
                return t < 1 ? "M" + points.map(function (p) { return p(t); }).join("L") : d1;
            };
        };
    };
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GraphComponent.prototype, "lineData", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GraphComponent.prototype, "pointData", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], GraphComponent.prototype, "height", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], GraphComponent.prototype, "width", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GraphComponent.prototype, "includeLineDataPoints", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GraphComponent.prototype, "includeHoverLine", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Function)
    ], GraphComponent.prototype, "hoverLineDisplay", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], GraphComponent.prototype, "transitionDuration", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GraphComponent.prototype, "hideBorder", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GraphComponent.prototype, "yAxisTitle", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GraphComponent.prototype, "ySecondAxisTitle", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Function)
    ], GraphComponent.prototype, "interpolationMethod", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Margin)
    ], GraphComponent.prototype, "margin", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GraphComponent.prototype, "xAxisTextRotation", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GraphComponent.prototype, "yAxisSecondAxisDataFilter", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GraphComponent.prototype, "AllowZoomX", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GraphComponent.prototype, "AllowZoomY", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GraphComponent.prototype, "xExtent", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GraphComponent.prototype, "IncludeDifference", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GraphComponent.prototype, "disableWheelZoom", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GraphComponent.prototype, "UseContinuousHoverLine", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GraphComponent.prototype, "xDomain", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GraphComponent.prototype, "yDomain", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GraphComponent.prototype, "useTweenTransition", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GraphComponent.prototype, "lineSizePx", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], GraphComponent.prototype, "pointSizeR", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GraphComponent.prototype, "userColors", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GraphComponent.prototype, "UniqueId", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], GraphComponent.prototype, "TooltipItemChange", void 0);
    __decorate([
        ViewChild('tooltip'),
        __metadata("design:type", ElementRef)
    ], GraphComponent.prototype, "tooltipElementRef", void 0);
    GraphComponent = __decorate([
        Component({
            selector: 'pm-graph',
            //templateUrl: './app/controls/components/graph/graph-component.html',
            templateUrl: './graph-component.html',
            styles: ["\n  :host { \n    position: relative;\n    display: block;\n  }"],
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ElementRef])
    ], GraphComponent);
    return GraphComponent;
}());
export { GraphComponent };
