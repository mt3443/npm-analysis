import { ColumnType } from '../../objects/request/column-type';
import { GridLength } from '../../objects/request/grid-length';
var Column = /** @class */ (function () {
    function Column(Key, Name, Property, Type, Width, CellTextAlign, HeaderTextAlign, CellTemplate, HeaderTemplate, DefaultValue, CellModules, HeaderComponents, HideFilter, HideResize, Aggregate, ColumnGroupName, Format) {
        this.Key = Key;
        this.Name = Name;
        this.Property = Property;
        this.Type = Type;
        this.Width = Width;
        this.CellTextAlign = CellTextAlign;
        this.HeaderTextAlign = HeaderTextAlign;
        this.CellTemplate = CellTemplate;
        this.HeaderTemplate = HeaderTemplate;
        this.DefaultValue = DefaultValue;
        this.CellModules = CellModules;
        this.HeaderComponents = HeaderComponents;
        this.HideFilter = HideFilter;
        this.HideResize = HideResize;
        this.Aggregate = Aggregate;
        this.ColumnGroupName = ColumnGroupName;
        this.Format = Format;
        this.DefaultValue = DefaultValue || "";
        this.HeaderTextAlign = HeaderTextAlign || this.DefaultHeaderTextAlign;
        this.CellTextAlign = CellTextAlign || this.DefaultCellTextAlign;
        this.HideFilter = Type.IsFill ? true : HideFilter;
    }
    Object.defineProperty(Column.prototype, "DefaultHeaderTextAlign", {
        get: function () {
            // if (this.Type.IsNumber || this.Type.IsDate || this.Type.IsDateTime)
            //     return "right";
            return "left";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Column.prototype, "DefaultCellTextAlign", {
        get: function () {
            if (this.Type.IsNumber ||
                this.Type.IsDate ||
                this.Type.IsDateTime ||
                this.Type.IsCurrency)
                return "right";
            return "left";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Column, "FillerColumn", {
        get: function () {
            return new Column("_filler", "", "", ColumnType.Fill, new GridLength(0), undefined, undefined, undefined, undefined, undefined, undefined, undefined, true, true, undefined, undefined);
        },
        enumerable: true,
        configurable: true
    });
    return Column;
}());
export { Column };
