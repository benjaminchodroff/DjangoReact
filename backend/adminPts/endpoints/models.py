from django.db import models

# Create your models here.

class rolPersona(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "roles de persona"



class tipoEvento(models.Model):
    nombre = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "tipos de evento"



class evento(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateTimeField(null=True)
    tipo = models.ForeignKey(tipoEvento, on_delete=models.CASCADE, related_name="eventos")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "eventos"



class tipoEstructura(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "tipos de estructura"



class zona(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "zonas"



class estructura(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(tipoEstructura, on_delete=models.CASCADE, related_name="estructuras")
    zona = models.ForeignKey(zona, on_delete=models.CASCADE, related_name="estructuras")
    # personas
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "estructuras"



class persona(models.Model):
    nombre = models.CharField(max_length=50)
    rol = models.ForeignKey(rolPersona, on_delete=models.CASCADE, related_name="personas")
    edad = models.PositiveSmallIntegerField(null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    estructura = models.ForeignKey(estructura, on_delete=models.CASCADE, related_name="personas", null=True)
    # aportes
    # relaciones_propias
    # relacion_de
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "personas"



class relacion(models.Model):
    persona_militante = models.ForeignKey(persona, on_delete=models.CASCADE, related_name="relaciones_propias")
    persona_contacto = models.ForeignKey(persona, on_delete=models.CASCADE, related_name="relacion_de")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Relación de " + self.persona_militante.nombre + " y " + self.persona_contacto.nombre

    class Meta:
        verbose_name_plural = "relaciones"



class tipoAporte(models.Model):
    nombre = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "tipos de aporte"


class mes(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.PositiveSmallIntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "meses"



class aporte(models.Model):
    tipoAporte = models.ForeignKey(tipoAporte, on_delete=models.CASCADE, related_name="aportes")
    mes = models.ForeignKey(mes, on_delete=models.CASCADE, related_name="aportes")
    persona = models.ForeignKey(persona, on_delete=models.CASCADE, related_name="aportes")
    monto = models.PositiveSmallIntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.monto

    class Meta:
        verbose_name_plural = "aportes"
