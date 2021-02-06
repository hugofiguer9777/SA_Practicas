import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UsuariosService {

  // Ruta general de la API
  API_URI = 'https://gorest.co.in/public-api';
  // Token generado en gorest.co
  auth_token = '92191436ee198f3d569d0d9a33a37d4cbc5187723afc3b839d0dd8275a900a45';
  headers = new HttpHeaders({
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${this.auth_token}`
  });

  constructor(private http: HttpClient) { }

  getUsuarios(page: any) {
    // Metodo GET para obtener los usuarios
    return this.http.get(`${this.API_URI}/users?page=${page}`);
  }

  getUsuario(id: any) {
    // Metodo GET:id para obtener la informacion de un usuario
    return this.http.get(`${this.API_URI}/users/${id}`);
  }

  nuevoUsuario(user: any) {
    // Metodo POST para guardar un usuario
    return this.http.post(`${this.API_URI}/users`, user, { headers: this.headers });
  }

  eliminarUsuario(id: any) {
    // Metodo DELETE para eliminar un usuario
    return this.http.delete(`${this.API_URI}/users/${id}`, { headers: this.headers });
  }

  actualizarUsuario(id: any, userMod: any){
    // Metodo PUT para actualizar informacion de un usuario
    return this.http.put(`${this.API_URI}/users/${id}`, userMod, { headers: this.headers });
  }
}
