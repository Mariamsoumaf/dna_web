from django.db import models


class DNAResult(models.Model):
    sequence = models.CharField(max_length=500)
    count_a = models.IntegerField()
    count_t = models.IntegerField()
    count_c = models.IntegerField()
    count_g = models.IntegerField()
    is_valid = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sequence} - {'Valid' if self.is_valid else 'Invalid'}"
