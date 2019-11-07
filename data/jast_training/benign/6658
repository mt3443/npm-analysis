import { Injectable } from '@angular/core';
import * as EXIF from 'exif-js';
var NgxPicaExifService = (function () {
    function NgxPicaExifService() {
    }
    NgxPicaExifService.prototype.getExifOrientedImage = function (image) {
        return new Promise(function (resolve, reject) {
            EXIF.getData(image, function () {
                var allExifMetaData = EXIF.getAllTags(image), exifOrientation = allExifMetaData.Orientation;
                if (exifOrientation) {
                    var canvas = document.createElement('canvas'), ctx = canvas.getContext('2d'), width = image.width, height = image.height;
                    if ([5, 6, 7, 8].indexOf(exifOrientation) > -1) {
                        canvas.width = height;
                        canvas.height = width;
                    }
                    else {
                        canvas.width = width;
                        canvas.height = height;
                    }
                    if (ctx) {
                        // transform context before drawing image
                        switch (exifOrientation) {
                            case 2:
                                ctx.transform(-1, 0, 0, 1, width, 0);
                                break;
                            case 3:
                                ctx.transform(-1, 0, 0, -1, width, height);
                                break;
                            case 4:
                                ctx.transform(1, 0, 0, -1, 0, height);
                                break;
                            case 5:
                                ctx.transform(0, 1, 1, 0, 0, 0);
                                break;
                            case 6:
                                ctx.transform(0, 1, -1, 0, height, 0);
                                break;
                            case 7:
                                ctx.transform(0, -1, -1, 0, height, width);
                                break;
                            case 8:
                                ctx.transform(0, -1, 1, 0, 0, width);
                                break;
                            default:
                                ctx.transform(1, 0, 0, 1, 0, 0);
                        }
                        // Draw img into canvas
                        ctx.drawImage(image, 0, 0, width, height);
                        var img_1 = new Image();
                        img_1.width = width;
                        img_1.height = height;
                        img_1.onload = function () {
                            resolve(img_1);
                        };
                        img_1.src = canvas.toDataURL();
                    }
                }
                else {
                    resolve(image);
                }
            });
        });
    };
    NgxPicaExifService.decorators = [
        { type: Injectable },
    ];
    /** @nocollapse */
    NgxPicaExifService.ctorParameters = function () { return []; };
    return NgxPicaExifService;
}());
export { NgxPicaExifService };
//# sourceMappingURL=ngx-pica-exif.service.js.map