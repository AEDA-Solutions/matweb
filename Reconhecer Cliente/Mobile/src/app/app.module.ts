import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';
import { SplashScreen } from '@ionic-native/splash-screen';
import { StatusBar } from '@ionic-native/status-bar';
import { BarcodeScanner } from '@ionic-native/barcode-scanner';
import { HttpModule } from '@angular/http';
import { MyApp } from './app.component';
import { RestProvider } from '../providers/rest/rest';
import { FormProvider } from '../providers/form/form';
import { CarrinhoPage } from '../pages/carrinho/carrinho';



@NgModule({
  declarations: [
    MyApp,
    CarrinhoPage, 
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    HttpModule,
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    CarrinhoPage,
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    RestProvider,
    FormProvider,
    BarcodeScanner
  ]
})
export class AppModule {}
