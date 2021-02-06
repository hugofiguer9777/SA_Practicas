import { Component, OnInit } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css']
})
export class FormularioComponent implements OnInit {

  // objeto con los datos para un usuario
  usuario: any = {
    name: '',
    email: '',
    gender: '',
    status: ''
  };
  editar: boolean = false;

  constructor(private servicioUsuario: UsuariosService, private router: Router, private activatedRouter: ActivatedRoute) { }

  ngOnInit(): void {
    const params = this.activatedRouter.snapshot.params; // obtenemos los parametros de la ruta
    if (params.id) {
      // Si tenemos el parametro id, es porque vamos a editar un usuario
      this.servicioUsuario.getUsuario(params.id).subscribe(
        res => {
          // Obtenemos los datos del usuario a editar
          this.usuario = res;
          this.usuario = this.usuario.data;
          this.editar = true;
        },
        err => {
          console.log(err);
        }
      );
    }
  }

  guardarUsuario(){
    // Llamando a la ruta para guardar un usuario
    this.servicioUsuario.nuevoUsuario(this.usuario).subscribe(
      res => {
        this.router.navigate(['/usuarios']); // Redirigiendo a la ruta inicial
      },
      err => {
        console.log(err);
      }
    )
  }

  editarUsuario(){
    // Eliminando parametros que no son necesarios
    delete this.usuario.created_at;
    delete this.usuario.updated_at;
    // Llamando a la ruta para editar un usuario
    this.servicioUsuario.actualizarUsuario(this.usuario.id, this.usuario).subscribe(
      res => {
        this.router.navigate(['/usuarios']); // Redirigiendo a la ruta inicial
      },
      err => {
        console.log(err);
      }
    );
  }
}
