var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
import { Component, NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { JitCompilerFactory } from '@angular/platform-browser-dynamic';
import { ControlsModule } from '../../../controls-module';
var JitComponent = /** @class */ (function () {
    function JitComponent() {
    }
    JitComponent.createComponent = function (template, modules) {
        var TemplateComponent = /** @class */ (function () {
            function TemplateComponent() {
            }
            TemplateComponent = __decorate([
                Component({ template: template })
            ], TemplateComponent);
            return TemplateComponent;
        }());
        var TemplateModule = /** @class */ (function () {
            function TemplateModule() {
            }
            TemplateModule = __decorate([
                NgModule({ declarations: [TemplateComponent], imports: modules ? [RouterModule, ControlsModule].concat(modules) : [RouterModule, ControlsModule] })
            ], TemplateModule);
            return TemplateModule;
        }());
        var mod = JitComponent.getJitCompiler().compileModuleAndAllComponentsSync(TemplateModule);
        var factory = mod.componentFactories.find(function (comp) {
            return comp.componentType === TemplateComponent;
        });
        return factory;
    };
    JitComponent.getJitCompiler = function () {
        if (!this.compiler)
            this.compiler = new JitCompilerFactory().createCompiler();
        return this.compiler;
    };
    return JitComponent;
}());
export { JitComponent };
