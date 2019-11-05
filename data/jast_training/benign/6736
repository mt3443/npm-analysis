var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = y[op[0] & 2 ? "return" : op[0] ? "throw" : "next"]) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [0, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
import { Component, ChangeDetectionStrategy, ChangeDetectorRef, EventEmitter, Input, Output, ViewContainerRef, ViewChild } from '@angular/core';
import * as _ from 'lodash';
import { DialogService } from '../../..//controls/services/dialog/dialog-service';
import { Dictionary } from '../../../objects/dictionary';
import { GridSelectionMode } from '../../../objects/enums/grid-selection-mode';
import { ColumnFilter } from '../../../controls/components/grid/filters/column-filter';
import { ColumnSort } from '../../../controls/components/grid/sorting/column-sort';
import { ColumnGrouping } from '../../../objects/request/column-grouping';
import { Column } from '../../../objects/request/column';
import { JitComponent } from '../../../controls/components/base/components/jit-component';
import { ColumnType } from '../../../objects/request/column-type';
import { ElementExtensions } from '../../../objects/extensions/element-extensions';
import { GridColumnRange } from '../../../controls/components/grid/grid-columns/grid-column-range';
import { GridSettingsDialog } from '../../../controls/components/grid/grid-settings/grid-settings-dialog';
import { GridExport } from '../../../controls/components/grid/grid-export/grid-export';
import { SortDirection } from '../../../objects/enums/sort-direction';
import { ControlsModule } from '../../../controls/controls-module';
var MILLISECONDS_TO_WAIT_ON_SCROLLING_BEFORE_RENDERING = 5;
var GridComponent = /** @class */ (function () {
    function GridComponent(changeDetectorRef, viewContainerRef, dialog) {
        this.changeDetectorRef = changeDetectorRef;
        this.viewContainerRef = viewContainerRef;
        this.dialog = dialog;
        this.SelectedRowChange = new EventEmitter();
        this.HeightPx = 0;
        this.WidthPx = 0;
        this.PanelWidthPx = 0;
        this.ShowRowNumbers = true;
        this.ShowFooter = false;
        this.ShowColumnGroups = false;
        this.GridSelectionMode = GridSelectionMode.Cell;
        this.Rows = new Array();
        this.VisibleRows = new Array();
        this.VisibleColumns = new Array();
        this.Filters = new Dictionary();
        this.Sorts = new Dictionary();
        this.ColumnGroupings = new Array();
        this.itemsSource = [];
        this.columns = new Dictionary();
        this.rowHeight = 30;
        this.columnHeaderHeight = 24;
        this.el = viewContainerRef.element.nativeElement;
    }
    Object.defineProperty(GridComponent.prototype, "Grid", {
        // to react to the width / height changes
        // @HostBinding('style.flex-grow')
        // @Input() FlexGrow: string;
        get: function () {
            return this;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "ItemsSource", {
        get: function () {
            return this.itemsSource;
        },
        set: function (value) {
            if (value === this.itemsSource)
                return;
            this.itemsSource = value;
            this.createCollectionView();
            this.handleVerticalScroll(this.ScrollTop);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "Columns", {
        get: function () {
            return this.columns;
        },
        set: function (value) {
            if (value) {
                for (var i = 0; i < value.Values.length; i++) {
                    var item = value.Values[i];
                    if (item.CellTemplate) {
                        item.CellTemplateComponent = JitComponent.createComponent(item.CellTemplate, item.CellModules);
                    }
                    else if (item.Type.IsBoolean) {
                        item.CellTemplate = "<pm-check-box class=\"control-center\" IsReadOnly=\"true\" [IsChecked]=\"Row['" + item.Property + "']\"></pm-check-box>";
                        item.CellTemplateComponent = JitComponent.createComponent(item.CellTemplate, item.CellModules);
                    }
                    if (item.HeaderTemplate) {
                        item.HeaderTemplateComponent = JitComponent.createComponent(item.HeaderTemplate, item.HeaderComponents);
                    }
                }
                if (value.Values.some(function (item) { return ColumnType.Fill == item.Type; }) == false)
                    value.add("_fill", Column.FillerColumn);
            }
            this.columns = value;
            this.calculateWidth();
            this.changeDetectorRef.detectChanges();
            //this.createCollectionView();
            //this.handleVerticalScroll(this.ScrollTop);
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "RowHeight", {
        get: function () {
            return this.rowHeight;
        },
        set: function (value) {
            this.rowHeight = value;
            if (this.Rows) {
                this.calculateRowHeights(this.Rows);
            }
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "ColumnHeaderHeight", {
        get: function () {
            return this.columnHeaderHeight;
        },
        set: function (value) {
            this.columnHeaderHeight = value;
        },
        enumerable: true,
        configurable: true
    });
    GridComponent.prototype.ngOnInit = function () {
        this.calculateWidth();
        this.ContainerWidth = ElementExtensions.width(this.gridColumnHorizontalContainer);
        this.ContainerHeight = ElementExtensions.height(this.gridTableScrollbarVerticalContainer);
        this.handleHorizontalScroll(0);
        this.handleVerticalScroll(0);
    };
    GridComponent.prototype.ngDoCheck = function () {
        if (this.ContainerHeight != ElementExtensions.height(this.gridTableScrollbarVerticalContainer)) {
            this.ContainerHeight = ElementExtensions.height(this.gridTableScrollbarVerticalContainer);
            this.handleVerticalScroll(this.ScrollTop);
        }
        if (this.ContainerWidth != ElementExtensions.width(this.gridColumnHorizontalContainer)) {
            this.SizeHorizontalScrollbar();
            this.ContainerWidth = ElementExtensions.width(this.gridColumnHorizontalContainer);
            this.handleHorizontalScroll(this.ScrollLeft);
        }
    };
    GridComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Columns']) {
            this.handleHorizontalScroll(this.ScrollLeft);
        }
        // if (changes['ItemsSource']) {
        // }
        // if (changes['FrozenColumnCount']) {
        // }
        // if (changes['HierarchyColumnIndex']) {
        // }
        // if (changes['HierarchyColumnProperty']) {
        // }
        // if (changes['ShowRowNumbers']) {
        // }
        // if (changes['ShowFooter']) {
        // }
        // if (changes['ShowColumnGroups']) {
        // }
    };
    Object.defineProperty(GridComponent.prototype, "RegularColumns", {
        get: function () {
            if (this.Columns) {
                var columns = [];
                for (var i = 0; i < this.Columns.Values.length; i++) {
                    var column = this.Columns.Values[i];
                    if (!column.IsHidden)
                        columns.push(column);
                }
                return columns.slice(this.FrozenColumnCount);
            }
            return [];
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "FrozenColumns", {
        get: function () {
            if (this.Columns && this.FrozenColumnCount > 0) {
                var columns = [];
                for (var i = 0; i < this.Columns.Values.length; i++) {
                    var column = this.Columns.Values[i];
                    if (!column.IsHidden)
                        columns.push(column);
                }
                return columns.slice(0, this.FrozenColumnCount);
            }
            return [];
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "RegularColumnGroupings", {
        get: function () {
            if (this.ColumnGroupings) {
                return this.ColumnGroupings;
            }
            return [];
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "FrozenColumnGroupings", {
        get: function () {
            if (this.ColumnGroupings) {
                return this.ColumnGroupings;
            }
            return [];
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "FrozenColumnWidthPx", {
        get: function () {
            var frozenColumns = this.FrozenColumns;
            if (frozenColumns.length > 0) {
                var width = 0;
                for (var i = 0; i < frozenColumns.length; i++) {
                    var column = frozenColumns[i];
                    width += column.Width.Value;
                }
                return width;
            }
            return 0;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "VerticalScrollbarTopPx", {
        get: function () {
            if (this.ShowColumnGroups) {
                return 23 + 24;
            }
            return 23;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridComponent.prototype, "VerticalScrollbarBottomPx", {
        get: function () {
            if (this.ShowFooter) {
                return 18 + 24;
            }
            return 18;
        },
        enumerable: true,
        configurable: true
    });
    GridComponent.prototype.createCollectionView = function () {
        if (!this.ItemsSource)
            return;
        var items = this.ItemsSource.slice();
        //this._isExpanded
        if (this.Filters.any()) {
            for (var i = 0; i < this.Filters.length; i++) {
                var filter = this.Filters.Values[i];
                items = items.filter(function (item) {
                    return filter.Filter(item);
                });
            }
        }
        if (this.Sorts.any()) {
            for (var i = 0; i < this.Sorts.length; i++) {
                var sort = this.Sorts.Values[i];
                items = items.sort(function (a, b) {
                    return sort.Sort(a, b);
                });
            }
        }
        if (items) {
            items = this.getAllItems(items);
            this.calculateRowHeights(items);
        }
        this.Rows = items;
        this.RowNumbers = Array.from(Array(this.Rows.length).keys());
        //this.calculateRowHeights(this.Rows);
    };
    GridComponent.prototype.onVerticalScroll = function (event) {
        var _this = this;
        var currentScrollTop = this.gridRowVerticalContainer.nativeElement.scrollTop = event.target.scrollTop;
        //this.handleVerticalScroll(currentScrollTop);
        setTimeout(function () {
            var latestScrollTop = _this.gridRowVerticalContainer.nativeElement.scrollTop;
            if (currentScrollTop !== latestScrollTop) {
                return;
            }
            _this.handleVerticalScroll(latestScrollTop);
        }, MILLISECONDS_TO_WAIT_ON_SCROLLING_BEFORE_RENDERING);
    };
    GridComponent.prototype.handleVerticalScroll = function (scrollTop) {
        return __awaiter(this, void 0, void 0, function () {
            var viewPortStartIndex, viewPortEndIndex;
            return __generator(this, function (_a) {
                this.ScrollTop = scrollTop;
                viewPortStartIndex = this.getViewPortStartIndex();
                viewPortEndIndex = this.getViewPortEndIndex(viewPortStartIndex);
                this.VisibleRows = this.Rows.slice(viewPortStartIndex, viewPortEndIndex);
                this.changeDetectorRef.detectChanges();
                return [2 /*return*/];
            });
        });
    };
    GridComponent.prototype.getViewPortStartIndex = function () {
        if (this.CalculateRowSize) {
            // do a binary search on the elements to find the first item.
            return Math.max(_(this.Rows).map(function (i) { return i._top; }).sortedIndex(this.ScrollTop) - 1, 0);
        }
        return Math.floor(this.ScrollTop / this.RowHeight);
    };
    GridComponent.prototype.getViewPortEndIndex = function (startIndex) {
        if (this.CalculateRowSize) {
            var i = startIndex;
            while (i < this.Rows.length && this.Rows[i]._top < this.ContainerHeight + this.ScrollTop)
                i++;
            return i;
        }
        return startIndex + Math.ceil(this.ContainerHeight / this.RowHeight) + 1;
    };
    GridComponent.prototype.onHorizontalScroll = function (event) {
        var _this = this;
        var currentScrollLeft = this.gridRowHorizontalContainer.nativeElement.scrollLeft
            = this.gridColumnHorizontalContainer.nativeElement.scrollLeft
                = event.target.scrollLeft;
        if (this.ShowFooter)
            this.gridFooterContainer.nativeElement.scrollLeft = event.target.scrollLeft;
        if (this.ShowColumnGroups)
            this.gridColumnGroupContainer.nativeElement.scrollLeft = event.target.scrollLeft;
        //this.handleHorizontalScroll(currentScrollLeft);
        setTimeout(function () {
            var latestScrollLeft = _this.gridRowHorizontalContainer.nativeElement.scrollLeft;
            if (currentScrollLeft !== latestScrollLeft) {
                return;
            }
            _this.handleHorizontalScroll(latestScrollLeft);
        }, MILLISECONDS_TO_WAIT_ON_SCROLLING_BEFORE_RENDERING);
    };
    GridComponent.prototype.handleHorizontalScroll = function (scrollLeft) {
        return __awaiter(this, void 0, void 0, function () {
            var width, columns, visibleColumns, visible, hidden;
            return __generator(this, function (_a) {
                this.ScrollLeft = scrollLeft;
                if (!this.Columns)
                    return [2 /*return*/];
                width = ElementExtensions.width(this.gridColumnHorizontalContainer) + scrollLeft + this.FrozenColumnWidthPx;
                this.FrozenColumns.forEach(function (c) { return c.IsVisible = true; });
                columns = this.RegularColumns;
                visibleColumns = GridColumnRange.GetVisibleColumns(columns, scrollLeft, width);
                if (this.VisibleColumns.length == 0) {
                    visibleColumns.forEach(function (c) { return c.IsVisible = true; });
                }
                else {
                    visible = _.difference(visibleColumns, this.VisibleColumns);
                    hidden = _.difference(this.VisibleColumns, visibleColumns);
                    visible.forEach(function (c) { return c.IsVisible = true; });
                    hidden.forEach(function (c) { return c.IsVisible = false; });
                }
                this.VisibleColumns = visibleColumns;
                this.changeDetectorRef.detectChanges();
                return [2 /*return*/];
            });
        });
    };
    GridComponent.prototype.calculateWidth = function () {
        var width = 0;
        var currentGroupName, columnGroupings = [], currentColumnGrouping;
        if (this.Columns) {
            for (var i = 0; i < this.Columns.Values.length; i++) {
                var column = this.Columns.Values[i];
                column['_columnNumber'] = i;
                if (!column.IsHidden) {
                    column['_left'] = width;
                    width += column.Width.Value;
                    column['_right'] = width;
                }
                if (column.Type.IsFill) {
                    var element1 = ElementExtensions.width(this.gridRowHorizontalContainer);
                    if (width < element1) {
                        var amount = element1 - width;
                        column['_left'] = width;
                        //width += 100;
                        column.Width.Value = amount;
                        width += column.Width.Value;
                        column['_right'] = width;
                    }
                    else if (column.Width.Value < 1) {
                        column.IsHidden = true;
                    }
                }
                if (this.ShowColumnGroups && this.ColumnGroups) {
                    if (column.ColumnGroupName == currentGroupName) {
                        currentColumnGrouping.Width.Value += column.Width.Value;
                    }
                    else {
                        currentGroupName = column.ColumnGroupName;
                        var group = this.ColumnGroups[currentGroupName];
                        if (group) {
                            currentColumnGrouping = new ColumnGrouping(group.Name, group.HeaderTextAlign);
                            currentColumnGrouping.Width.Value = column.Width.Value;
                            columnGroupings.push(currentColumnGrouping);
                        }
                    }
                }
            }
            if (this.ShowColumnGroups && columnGroupings) {
                this.ColumnGroupings = columnGroupings;
            }
        }
        this.WidthPx = width;
        this.SizeHorizontalScrollbar();
    };
    GridComponent.prototype.SizeHorizontalScrollbar = function () {
        var panel = ElementExtensions.width(this.gridTableScrollbarHorizontalScrollPanel);
        var container = ElementExtensions.width(this.gridTableScrollbarHorizontalContainer);
        var diff = container - panel;
        this.PanelWidthPx = this.WidthPx - diff;
    };
    GridComponent.prototype.getAllItems = function (items) {
        if (this.HierarchyColumnProperty && items) {
            var all = [];
            for (var i = 0; i < items.length; i++) {
                var item = items[i];
                all.push(item);
                if (item['_isExpanded']) {
                    var children = this.getAllItems(item[this.HierarchyColumnProperty]);
                    all.push.apply(all, children);
                }
            }
            return all;
        }
        return items;
    };
    GridComponent.prototype.calculateRowHeights = function (items) {
        var totalHeight = 0;
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            item['_top'] = totalHeight;
            item['_rowNumber'] = i + 1;
            if (item['_rowResizeHeight'])
                item['_rowHeight'] = item['_rowResizeHeight'];
            else if (this.CalculateRowSize)
                item['_rowHeight'] = this.CalculateRowSize(item);
            else
                item['_rowHeight'] = this.RowHeight;
            totalHeight += item['_rowHeight'];
        }
        this.HeightPx = totalHeight;
    };
    GridComponent.prototype.showSettings = function () {
        GridSettingsDialog.Show(this);
    };
    GridComponent.prototype.mouseWheelUp = function (event) {
        this.gridTableScrollbarVerticalContainer.nativeElement.scrollTop -= event.wheelDelta;
    };
    GridComponent.prototype.mouseWheelDown = function (event) {
        this.gridTableScrollbarVerticalContainer.nativeElement.scrollTop -= event.wheelDelta;
    };
    GridComponent.prototype.ExportToExcel = function () {
        var gridExport = new GridExport();
        gridExport.ExportToXlsx(this, "export");
    };
    GridComponent.prototype.SetRowFocus = function (row) {
        var rowFocus = {};
        rowFocus[row['_rowNumber']] = true;
        this.RowFocus = rowFocus;
        var columnFocus = {};
        for (var i = 0; i < this.Columns.length; i++) {
            var column = this.Columns.Values[i];
            columnFocus[column.Key] = true;
        }
        this.ColumnFocus = columnFocus;
    };
    GridComponent.prototype.SetColumnFocus = function (row, column) {
        var rowFocus = {};
        rowFocus[row['_rowNumber']] = true;
        this.RowFocus = rowFocus;
        var columnFocus = {};
        columnFocus[column.Key] = true;
        this.ColumnFocus = columnFocus;
    };
    GridComponent.prototype.SelectRow = function (row) {
        var rows = {};
        rows[row['_rowNumber']] = true;
        this.SetRowFocus(row);
        this.SelectedCells = {};
        this.SelectedRows = rows;
        this.SelectedRow = row;
        this.SelectedRowChange.emit(this.SelectedRow);
        this.changeDetectorRef.detectChanges();
    };
    GridComponent.prototype.SelectCell = function (cell) {
        if (this.GridSelectionMode == GridSelectionMode.Row) {
            this.SelectRow(cell.Row);
            return;
        }
        var cells = {};
        cells[cell.Row['_rowNumber'] + cell.Column.Key] = true;
        cells[cell.Row['_rowNumber']] = true;
        this.SetColumnFocus(cell.Row, cell.Column);
        this.SelectedCells = cells;
        var rows = {};
        //rows[cell.Row['_rowNumber']] = true;
        this.SelectedCell = cell;
        this.SelectedRows = rows;
        this.SelectedRow = cell.Row;
        this.SelectedRowChange.emit(this.SelectedRow);
        this.changeDetectorRef.detectChanges();
    };
    GridComponent.prototype.ExpandCollapseHierarchyRow = function (row) {
        row['_isExpanded'] = !row['_isExpanded'];
        if (this.Rows) {
            this.createCollectionView();
            this.RefreshGrid();
        }
    };
    GridComponent.prototype.ShowHideColumn = function (column) {
        column.IsHidden = !column.IsHidden;
        this.calculateWidth();
        this.handleHorizontalScroll(this.ScrollLeft);
    };
    GridComponent.prototype.ResizeColumn = function (column) {
        this.calculateWidth();
        this.handleHorizontalScroll(this.ScrollLeft);
    };
    GridComponent.prototype.ResizeRow = function (row) {
        this.calculateRowHeights(this.Rows);
        this.handleVerticalScroll(this.ScrollTop);
    };
    GridComponent.prototype.SetFilter = function (column, filterValue, searchType, selectedDistinctValues) {
        if (this.Filters.containsKey(column.Key)) {
            this.Filters.remove(column.Key);
        }
        column['_hasFilter'] = true;
        column['_selectedDistinctValues'] = selectedDistinctValues;
        this.Filters.add(column.Key, new ColumnFilter(column, filterValue, searchType, selectedDistinctValues));
        this.createCollectionView();
        this.handleVerticalScroll(this.ScrollTop);
    };
    GridComponent.prototype.ClearFilter = function (column) {
        if (this.Filters.containsKey(column.Key)) {
            column['_hasFilter'] = false;
            this.Filters.remove(column.Key);
        }
        this.createCollectionView();
        this.handleVerticalScroll(this.ScrollTop);
    };
    GridComponent.prototype.SetSort = function (column, direction) {
        if (this.Sorts.containsKey(column.Key)) {
            var sort = this.Sorts[column.Key];
            if (sort.Direction == direction) {
                column['_hasSort'] = undefined;
                this.Sorts.remove(column.Key);
            }
            else {
                sort.Direction = direction;
                column['_hasSort'] = { direction: direction };
            }
        }
        else {
            this.Sorts.add(column.Key, new ColumnSort(column, direction));
            column['_hasSort'] = { direction: direction };
        }
        this.createCollectionView();
        this.handleVerticalScroll(this.ScrollTop);
    };
    GridComponent.prototype.ToggleSort = function (column) {
        // When toggling the sort order, the column will go from No Sort -> Ascending -> Descending -> No Sort.
        if (this.Sorts.containsKey(column.Key)) {
            var sort = this.Sorts[column.Key];
            if (sort.Direction == SortDirection.Descending) {
                // Remove the sort because the order is on Descending.
                column['_hasSort'] = undefined;
                this.Sorts.remove(column.Key);
            }
            else {
                // Because there is an existing sort and it's not descending, then the current sort must be ascending.
                // So, flip it to descending.
                sort.Direction = SortDirection.Descending;
                column['_hasSort'] = { direction: SortDirection.Descending };
            }
        }
        else {
            // There was no existing sort order. So, start with ascending.
            this.Sorts.add(column.Key, new ColumnSort(column, SortDirection.Ascending));
            column['_hasSort'] = { direction: SortDirection.Ascending };
        }
        this.createCollectionView();
        this.handleVerticalScroll(this.ScrollTop);
    };
    GridComponent.prototype.ExpandAll = function () {
        if (this.ItemsSource) {
            var items = this.ItemsSource.slice();
            for (var i = 0; i < items.length; i++) {
                var item = items[i];
                item['_isExpanded'] = true;
            }
            this.createCollectionView();
            this.RefreshGrid();
        }
    };
    GridComponent.prototype.CollapseAll = function () {
        if (this.ItemsSource) {
            var items = this.ItemsSource.slice();
            for (var i = 0; i < items.length; i++) {
                var item = items[i];
                item['_isExpanded'] = false;
            }
            this.createCollectionView();
            this.RefreshGrid();
        }
    };
    GridComponent.prototype.ToggleHighlightRow = function (row) {
        row['_isHighlighted'] = true;
        this.RaiseChange();
    };
    GridComponent.prototype.RaiseChange = function () {
        this.changeDetectorRef.detectChanges();
    };
    GridComponent.prototype.RefreshGrid = function () {
        this.handleHorizontalScroll(this.ScrollLeft);
        this.handleVerticalScroll(this.ScrollTop);
    };
    Object.defineProperty(GridComponent.prototype, "IsDevMode", {
        get: function () {
            return ControlsModule.IsDevMode;
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GridComponent.prototype, "GridClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "SelectedCell", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "SelectedRow", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], GridComponent.prototype, "SelectedRowChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "SelectedCells", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "SelectedRows", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "RowFocus", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "ColumnFocus", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "HeightPx", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "WidthPx", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "PanelWidthPx", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], GridComponent.prototype, "FrozenColumnCount", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], GridComponent.prototype, "HierarchyColumnIndex", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "HierarchyColumnProperty", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GridComponent.prototype, "ShowRowNumbers", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GridComponent.prototype, "ShowFooter", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GridComponent.prototype, "ShowColumnGroups", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Dictionary)
    ], GridComponent.prototype, "ColumnGroups", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "ContextMenu", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GridComponent.prototype, "LastColumnFill", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GridComponent.prototype, "HideRowResize", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Function)
    ], GridComponent.prototype, "CalculateRowSize", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GridComponent.prototype, "CellMouseOver", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GridComponent.prototype, "RowMouseOver", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GridComponent.prototype, "GridSelectionMode", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GridComponent.prototype, "IsBusy", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], GridComponent.prototype, "BusyMessage", void 0);
    __decorate([
        ViewChild('gridRowVerticalContainer'),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "gridRowVerticalContainer", void 0);
    __decorate([
        ViewChild('gridRowHorizontalContainer'),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "gridRowHorizontalContainer", void 0);
    __decorate([
        ViewChild('gridColumnHorizontalContainer'),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "gridColumnHorizontalContainer", void 0);
    __decorate([
        ViewChild('gridColumnGroupContainer'),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "gridColumnGroupContainer", void 0);
    __decorate([
        ViewChild('gridFooterContainer'),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "gridFooterContainer", void 0);
    __decorate([
        ViewChild('gridTableScrollbarHorizontalContainer'),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "gridTableScrollbarHorizontalContainer", void 0);
    __decorate([
        ViewChild('gridTableScrollbarVerticalContainer'),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "gridTableScrollbarVerticalContainer", void 0);
    __decorate([
        ViewChild('gridTableScrollbarHorizontalScrollPanel'),
        __metadata("design:type", Object)
    ], GridComponent.prototype, "gridTableScrollbarHorizontalScrollPanel", void 0);
    __decorate([
        Input('ItemsSource'),
        __metadata("design:type", Array),
        __metadata("design:paramtypes", [Array])
    ], GridComponent.prototype, "ItemsSource", null);
    __decorate([
        Input('Columns'),
        __metadata("design:type", Dictionary),
        __metadata("design:paramtypes", [Dictionary])
    ], GridComponent.prototype, "Columns", null);
    __decorate([
        Input('RowHeight'),
        __metadata("design:type", Number),
        __metadata("design:paramtypes", [Number])
    ], GridComponent.prototype, "RowHeight", null);
    __decorate([
        Input('ColumnHeaderHeight'),
        __metadata("design:type", Number),
        __metadata("design:paramtypes", [Number])
    ], GridComponent.prototype, "ColumnHeaderHeight", null);
    GridComponent = __decorate([
        Component({
            selector: 'pm-grid',
            //templateUrl: './app/controls/components/grid/grid.html',
            templateUrl: './grid.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            ViewContainerRef,
            DialogService])
    ], GridComponent);
    return GridComponent;
}());
export { GridComponent };
