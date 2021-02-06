import { Component, OnInit } from '@angular/core';

import { UsuariosService } from '../../services/usuarios.service';

@Component({
  selector: 'app-lista',
  templateUrl: './lista.component.html',
  styleUrls: ['./lista.component.css']
})
export class ListaComponent implements OnInit {

  objetoUsers: any;
  usuarios: any = [];
  pages: any = [];
  totalPaginas = 0;
  paginaActual = 1;

  constructor(private servicioUsuarios: UsuariosService) { }

  ngOnInit(): void {
    // Llamada al metodo GET para obtener informacion inicial de la primera pagina de usuarios
    this.getUsuarios(1);
  }

  actualizar(page: any){
    // Llamada para obtener los usuarios de una pagina especifica
    this.paginaActual = page;
     // Realizando una nueva llamada con los datos de la pagina en especifico
    this.getUsuarios(page);
  }

  eliminarUsuario(iduser: any) {
    // Llamada para eliminar un usuario
    this.servicioUsuarios.eliminarUsuario(iduser).subscribe(
      res => {
        // Respuesta correcta por parte de la API
        // Realizando un nuevo GET para actualizar la vista
        this.getUsuarios(this.paginaActual);
      },
      err => {
        console.log(err);
      }
    );
  }

  getUsuarios(pagina: any) {
    // Realizando un nuevo GET para actualizar la vista
    this.servicioUsuarios.getUsuarios(pagina).subscribe(
      res => {
        // Respuesta correcta por parte de la API
        this.objetoUsers = res;
        this.usuarios = this.objetoUsers.data;
        this.totalPaginas = this.objetoUsers.meta.pagination.pages; // obtenemos el total de paginas
        for (let index = 0; index < this.totalPaginas; index++) { // iteracion para llenar una lista con los numeros
          this.pages[index] = index+1;
        }
      },
      err => {
        // Posible error al realizar la consulta
        console.log(err);
      }
    );
  }

}
