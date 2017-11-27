Export to Render Farm

Esta herramienta hace prácticamente lo que literalmente dice su nombre, pero a diferencia del "Collect Files" original de cinema tiene algunos features principales por la cual la preferimos:

-Agiliza flujos de collect y render files: lo esencial de este script es agilizar el flujo de realizar collects para rendearlos entre varias maquinas o subirlo a una granja de render.

Como nosotros disponemos de un servidor siempre dejamos los collect en el servidor para que las distintas maquinas puedan rendearlo, por el lado de las granjas de render online la mayoría tiene su propio plug in que ya hace esto.

-Mantiene la escena original: a diferencia del collect original, al hacer el collect no te cierra tu escena original y deja abierta la nueva, por el contrario, no abre la escena nueva simplemente se sigue trabajando en la original.

-Rutas inteligentes de render: aprovechando los tokens de render de cinema y usando la correcta nomenclatura en los archivos originales, no hay que escribir las rutas de render ya que hace una carpeta con el nombre del proyecto donde guarda el beauty y el multipass exr ($prj_Beauty / $prj_MP). Así evitamos errores de escritura de archivos también.

*Si el motor de render es Arnold el beauty (Regular image) estará en Arnold Dummy para no guardar ningún archivo ya que en los AOVs sale el beauty.

https://scontent.fscl9-1.fna.fbcdn.net/v/t31.0-8/12265718_10153356726913937_5124077204262922152_o.jpg?oh=8edec013be4c94f76be0f4e806acea2f&oe=5AA35FA0
