from django.db import models


class KitchenStyle(models.Model):
    name = models.CharField('Наименование', max_length=50)

    class Meta:
        verbose_name = "Стиль кухни"
        verbose_name_plural = "Стили кухни"

    def __str__(self):
        return self.name


class KitchenMaterial(models.Model):
    name = models.CharField('Наименование', max_length=50)
    kitchen_styles = models.ForeignKey(KitchenStyle, on_delete=models.CASCADE, verbose_name="Вид кухни")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.name


class KitchenOpeningMethod(models.Model):
    name = models.CharField('Наименование', max_length=50)
    kitchen_styles = models.ForeignKey(KitchenStyle, on_delete=models.CASCADE, verbose_name="Вид кухни")

    class Meta:
        verbose_name = "Способ открытия"
        verbose_name_plural = "Способы открытия"

    def __str__(self):
        return self.name


class Kitchen(models.Model):
    name = models.CharField('Наименование', max_length=50)
    style = models.ForeignKey(KitchenStyle, on_delete=models.CASCADE, verbose_name="Вид кухни", related_name='kitchens')
    material = models.ForeignKey(KitchenMaterial, on_delete=models.CASCADE, verbose_name="Материал кухни")
    openingMethod = models.ForeignKey(KitchenOpeningMethod, on_delete=models.CASCADE, verbose_name="Метод открытия")

    class Meta:
        verbose_name = "Кухня"
        verbose_name_plural = "Кухни"

