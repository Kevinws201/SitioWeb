from django.test import TestCase
from .models import CustomUser
from django.urls import reverse
from .forms import CustomUserCreationForm
from myapp.models import CustomUser
# Create your tests here.


class CustomUserModelTest(TestCase):
    def setUp(self):
        # Configuración inicial para los casos de prueba
        self.user = CustomUser.objects.create(
            username="testuser",
            email="testuser@example.com",
            carrera="Sistemas Computacionales",
            nivel_educativo="LIC"
        )
    
    def test_user_creation(self):
        # Verificar si el usuario fue creado correctamente
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")
    
    def test_user_carrera(self):
        # Verificar que el campo carrera sea correcto
        self.assertEqual(self.user.carrera, "Sistemas Computacionales")


class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

class CustomUserCreationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'strongpassword',
            'password2': 'strongpassword',
            'carrera': 'Sistemas Computacionales',
            'nivel_educativo': 'LIC'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

class RegisterViewTest(TestCase):
    def test_register_user_successfully(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        })
        self.assertEqual(response.status_code, 302)  # Redirección exitosa
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())
