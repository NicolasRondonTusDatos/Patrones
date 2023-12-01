# Singleton Pattern 
Singleton es un patrón de diseño creacional que nos permite asegurarnos 
de que una clase tenga una única instancia, 
a la vez que proporciona un punto de acceso global a dicha instancia.

Imagina que tienes un control remoto de televisión. En este caso, el control remoto es como una clase en programación, y la televisión es el objeto que pertenece a esa clase. Ahora, si varias personas en la misma habitación intentan usar el control remoto para cambiar el canal de la televisión, podría haber un problema de sincronización. Cada persona podría estar cambiando el canal al mismo tiempo, lo que sería confuso y poco práctico.

El patrón Singleton es como tener un solo control remoto para todos en la habitación. Solo hay una instancia (un único control remoto) que todos comparten. Cuando alguien quiere cambiar el canal, toma ese único control remoto, lo usa y, cuando termina, lo devuelve para que otros puedan usarlo. Esto garantiza que no haya conflictos ni problemas de sincronización, ya que solo existe una instancia del control remoto.

En resumen, el patrón Singleton se utiliza en programación para garantizar que solo haya una única instancia de una clase y proporciona un punto de acceso global a esa instancia, de manera similar a cómo un único control remoto se comparte entre varias personas para controlar una televisión en una habitación.