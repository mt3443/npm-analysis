var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Directive, HostListener, Input } from '@angular/core';
import { ContextMenuComponent } from '../../components/context-menu/context-menu-component';
var PopupMenuDirective = /** @class */ (function () {
    function PopupMenuDirective() {
    }
    PopupMenuDirective.prototype.onPopupMenu = function (event) {
        this.popupMenu.DataContext = this.popupMenuDataContext;
        this.popupMenu.ContextMenuTemplate = this.popupContextMenuTemplate;
        this.popupMenu.Show(event.clientX, event.clientY);
        event.preventDefault();
        event.stopPropagation();
    };
    __decorate([
        Input(),
        __metadata("design:type", ContextMenuComponent)
    ], PopupMenuDirective.prototype, "popupMenu", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], PopupMenuDirective.prototype, "popupMenuDataContext", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], PopupMenuDirective.prototype, "popupContextMenuTemplate", void 0);
    __decorate([
        HostListener('click', ['$event']),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [MouseEvent]),
        __metadata("design:returntype", void 0)
    ], PopupMenuDirective.prototype, "onPopupMenu", null);
    PopupMenuDirective = __decorate([
        Directive({
            selector: '[popupMenu]',
        })
    ], PopupMenuDirective);
    return PopupMenuDirective;
}());
export { PopupMenuDirective };
