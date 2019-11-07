import { NgModule } from '@angular/core';
import { NgxPicaService } from './ngx-pica.service';
import { NgxPicaExifService } from './ngx-pica-exif.service';
import { NgxPicaImageService } from './ngx-pica-image.service';
var NgxPicaModule = (function () {
    function NgxPicaModule() {
    }
    NgxPicaModule.decorators = [
        { type: NgModule, args: [{
                    providers: [
                        { provide: NgxPicaService, useClass: NgxPicaService },
                        { provide: NgxPicaExifService, useClass: NgxPicaExifService },
                        { provide: NgxPicaImageService, useClass: NgxPicaImageService },
                    ]
                },] },
    ];
    /** @nocollapse */
    NgxPicaModule.ctorParameters = function () { return []; };
    return NgxPicaModule;
}());
export { NgxPicaModule };
//# sourceMappingURL=ngx-pica.module.js.map