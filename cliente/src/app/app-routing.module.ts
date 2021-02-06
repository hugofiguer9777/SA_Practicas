import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FormularioComponent } from './components/formulario/formulario.component';
import { ListaComponent } from './components/lista/lista.component';

const routes: Routes = [
  {
    // Ruta inicial de la aplicacion
    path: '',
    redirectTo: '/usuarios',
    pathMatch: 'full'
  },
  {
    // Ruta de la lista de usuarios
    path: 'usuarios',
    component: ListaComponent
  },
  {
    // Ruta para agregar un nuevo usuario
    path: 'usuario/add',
    component: FormularioComponent
  },
  {
    // Ruta para editar un usuario
    path: 'usuario/edit/:id',
    component: FormularioComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
