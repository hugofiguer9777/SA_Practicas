import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavigationComponent } from './components/navigation/navigation.component';
import { FormularioComponent } from './components/formulario/formulario.component';
import { ListaComponent } from './components/lista/lista.component';

import { UsuariosService } from './services/usuarios.service';

@NgModule({
  declarations: [
    AppComponent,
    NavigationComponent,
    FormularioComponent,
    ListaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    UsuariosService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
