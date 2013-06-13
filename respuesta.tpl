<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <title>Buscador de empleo</title>
      <link rel="stylesheet" type="text/css" href="/home/ale/Escritorio/bottle/style/view.css" media="all">
	<script type="text/javascript" src="view.js"></script>
	
      </head>
      <body>
	<img src="/home/ale/Escritorio/bottle/style/foto.jpg" alt="image" title="image" />
	<table>
	  <tr>
	    <td><strong>Referencia</strong></td>
	    <td><strong>Empresa</strong></td>
	    <td><strong>Localizacion</strong></td>
	    <td><strong>Puesto de trabajo</strong></td>
	    <td><strong>Numero de vacantes</strong></td>
	  </tr>
	%for i in xrange(0,ofertas):
	<tr>
	 <td><a href="http://www.workmunity.com/position/{{referencias[i]}}">{{referencias[i]}}</a></td>
	 <td>{{empresas[i]}}</td>
	 <td>{{lugares[i]}}</td>
 	 <td>{{puestos[i]}}</td>
	 <td>{{vacantes[i]}}</td>
	</tr>
	%end
	</table>
	<br/>
	<form><input type='button' value='Atrás' name='Volver' onclick='history.back()' /></form>
      </body>
    </html>
	  
