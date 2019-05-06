from django.db import models

class  CurseManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(models.Q(name__icontains=query)|  models.Q (description__icontains=query))

class Curses(models.Model):
	name = models.CharField('Nome',max_length=100) 
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição Simples', blank=True)
	about = models.TextField('Sobre o curso',blank=True)
	start_date = models.DateField('Data de Inicio', null=True, blank=True)
	image = models.ImageField(upload_to='curses/images', verbose_name='Imagem', null=True, blank=True)
	created_at = models.DateTimeField('Criado em',auto_now_add=True)
	update_at = models.DateTimeField('Atualizado em', auto_now=True) 


	objects= CurseManager()

	def __str__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return ('curses:details',() , {'slug': self.slug})

	class Meta:
		verbose_name='Curso'
		verbose_name_plural='Cursos'
		ordering=['name']

# Create your models here.
