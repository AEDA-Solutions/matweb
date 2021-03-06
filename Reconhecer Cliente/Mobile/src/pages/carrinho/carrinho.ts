import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, LoadingController } from 'ionic-angular';
import { BarcodeScanner, BarcodeScannerOptions } from '@ionic-native/barcode-scanner';
import { RestProvider } from '../../providers/rest/rest';
import 'rxjs/add/operator/map';
import { FormProvider } from '../../providers/form/form';


@IonicPage()
@Component({
  selector: 'page-carrinho',
  templateUrl: 'carrinho.html',
  providers: [
    RestProvider
  ]
})
export class CarrinhoPage {

  options: BarcodeScannerOptions;
  results: {};
  private produtos = new Array<any>();

  constructor(public navCtrl: NavController,
    public navParams: NavParams,
    private barcodeScanner: BarcodeScanner,
    public rest: RestProvider,
    public form: FormProvider,
    public loadingCtrl: LoadingController,

  ) {
  }

  ionViewDidLoad() {
    this.getList();
  }

  public teste() {
    let data = {
      hash : "2ce506e29f6d4"
    }
    this.getProduto(data);
  }

  
  //Faz a leitura do código de barras e chama o método getProduto()
  public scanBarcode() {
    this.barcodeScanner.scan().then(results => {
      let data = {
        hash : results.text
      }
      this.getProduto(data);

    },
      error => {

      });

  }

  //Requisita ao servidor as informações de um produto a partir do seu código de barras
  private getProduto(data: any) {
    this.rest.postProduto(data).subscribe(
      data => {
        var produto = {
          
          name: data.name,
          id: data.id,
        }
        if (this.procurarProduto(produto.id) == -1) {//Verifica se o produto já foi adicionado à lista
          this.produtos.push(produto);//Adiciona à lista de produtos
          this.saveList();
          
        } else {
          this.form.presentToast('Carrinho do Cliente já está em proceso.');
        }
      }, error => {
        this.form.presentToast('Falha ao reconhecer cliente');
      });
  }

  //Procura um produto a partir da chave id do produto
  private procurarProduto(id) {
    for (var _i = 0; _i < this.produtos.length; _i++) {
      var produto = this.produtos[_i];
      if (produto.id == id) {
        return _i;
      }
    }
    return -1;
  }
  //Retira um produto a partir do seu id
  public retirar(id) {
    var index = this.procurarProduto(id);
    if (index != -1) {
      this.produtos.splice(index, 1);
      // this.saveList();
    }
  }

  //Salva a lista no provider
  public saveList(){
    this.form.setProductsList(this.produtos);
    console.log(this.produtos[0]);
  }

  //Pega a lista salva no provider
  public getList(){
    this.produtos = this.form.getProductsList();
  }
}
