# 📚 Documentación Completa de Windows-Use

<div align="center">

**Guía completa para configurar y utilizar el agente de automatización Windows-Use**

[English](README.md) | [Español](DOCUMENTACION.md)

</div>

---

## 📑 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Herramientas Operativas](#herramientas-operativas)
4. [Configuración de Modelos LLM](#configuración-de-modelos-llm)
5. [Sistema de Visión](#sistema-de-visión)
6. [Opciones de Configuración del Agente](#opciones-de-configuración-del-agente)
7. [Ejemplos de Uso Avanzado](#ejemplos-de-uso-avanzado)
8. [Solución de Problemas](#solución-de-problemas)

---

## Introducción

**Windows-Use** es un agente de automatización avanzado que puede interactuar directamente con el sistema operativo Windows a través de su interfaz gráfica (GUI). El agente utiliza modelos de lenguaje grandes (LLM) para comprender instrucciones en lenguaje natural y ejecutar acciones automatizadas en el escritorio.

### Características Principales

- ✅ **Interacción GUI Completa**: Control de mouse, teclado, y elementos de la interfaz
- ✅ **Gestión de Aplicaciones**: Lanzar, redimensionar y cambiar entre aplicaciones
- ✅ **Ejecución de Comandos**: PowerShell para operaciones del sistema
- ✅ **Memoria Persistente**: Sistema de archivos para guardar contexto entre tareas
- ✅ **Soporte Multi-LLM**: Compatible con 12 proveedores diferentes
- ✅ **Sistema de Visión Opcional**: Permite al agente "ver" capturas de pantalla

---

## Arquitectura del Sistema

### Módulos Principales

```
windows_use/
├── agent/              # Núcleo del agente
│   ├── desktop/       # Interacciones de bajo nivel con Windows
│   ├── tree/          # Conversión del árbol de accesibilidad
│   ├── registry/      # Gestión de herramientas
│   ├── prompt/        # Generación dinámica de prompts
│   └── tools/         # Implementaciones de herramientas
├── llms/              # Proveedores de modelos LLM
├── messages/          # Formatos de mensajes
├── telemetry/         # Registro y analíticas
└── tool/              # Infraestructura base de herramientas
```

### Flujo de Ejecución

1. **Inicialización**: El agente se configura con un LLM y opciones
2. **Observación**: Captura el estado del escritorio (árbol de accesibilidad)
3. **Razonamiento**: El LLM decide qué acciones tomar
4. **Acción**: Ejecuta herramientas para interactuar con Windows
5. **Iteración**: Repite hasta completar la tarea o alcanzar el límite de pasos

---

## Herramientas Operativas

El agente tiene acceso a 14 herramientas especializadas para interactuar con Windows. Para ver la lista completa detallada de herramientas con ejemplos, consulta [AGENTS.md](AGENTS.md).

### Resumen de Herramientas Disponibles

| Herramienta | Descripción | Uso Principal |
|-------------|-------------|---------------|
| **Click Tool** | Clics de mouse en coordenadas | Interacción con botones y elementos UI |
| **Type Tool** | Escritura de texto | Llenar formularios y campos de texto |
| **Scroll Tool** | Desplazamiento vertical/horizontal | Navegar contenido largo |
| **Drag Tool** | Arrastrar y soltar | Mover archivos, redimensionar ventanas |
| **Move Tool** | Mover cursor sin clic | Hover para tooltips |
| **Shortcut Tool** | Atajos de teclado | Acciones rápidas (Ctrl+C, Alt+Tab, etc.) |
| **Wait Tool** | Pausar ejecución | Esperar carga de aplicaciones |
| **App Tool** | Gestión de aplicaciones | Lanzar, cambiar, redimensionar apps |
| **Shell Tool** | Comandos PowerShell | Operaciones del sistema |
| **Memory Tool** | Almacenamiento persistente | Guardar contexto entre tareas |
| **Scrape Tool** | Extracción de contenido web | Leer páginas web |
| **Multi Select Tool** | Selección múltiple | Seleccionar varios archivos/elementos |
| **Multi Edit Tool** | Edición en lote | Llenar múltiples campos |
| **Done Tool** | Finalizar tarea | Señalar completación exitosa |

---

## Configuración de Modelos LLM

Windows-Use es compatible con 12 proveedores de LLM diferentes. A continuación las configuraciones más comunes:

### 1. Google Gemini

**Modelos recomendados:** `gemini-2.5-flash`, `gemini-2.5-flash-lite`

```python
from windows_use.llms.google import ChatGoogle
from windows_use.agent import Agent, Browser

api_key = "YOUR_GOOGLE_API_KEY"
llm = ChatGoogle(
    model="gemini-2.5-flash",
    api_key=api_key,
    temperature=0.7
)

agent = Agent(llm=llm, browser=Browser.EDGE)
```

### 2. Anthropic Claude

**Modelos recomendados:** `claude-sonnet-4-5`, `claude-opus-4`

```python
from windows_use.llms.anthropic import ChatAnthropic

api_key = "YOUR_ANTHROPIC_API_KEY"
llm = ChatAnthropic(
    model="claude-sonnet-4-5",
    api_key=api_key,
    temperature=0.7,
    max_tokens=8192
)

agent = Agent(llm=llm, browser=Browser.EDGE)
```

### 3. OpenAI

**Modelos recomendados:** `gpt-4-turbo`, `gpt-4o`

```python
from windows_use.llms.openai import ChatOpenAI

api_key = "YOUR_OPENAI_API_KEY"
llm = ChatOpenAI(
    model="gpt-4-turbo",
    api_key=api_key,
    temperature=0.7
)

agent = Agent(llm=llm, browser=Browser.CHROME)
```

### 4. Azure OpenAI

```python
from windows_use.llms.azure_openai import ChatAzureOpenAI

llm = ChatAzureOpenAI(
    endpoint="https://your-resource.openai.azure.com/",
    deployment_name="gpt-4-deployment",
    api_key="YOUR_AZURE_API_KEY",
    model="gpt-4",
    api_version="2025-01-01-preview",
    temperature=0.7
)

agent = Agent(llm=llm, browser=Browser.EDGE)
```

### 5. Ollama (Modelos Locales)

**Modelos recomendados:** `qwen3-vl:235b-cloud`, `llama3`, `mistral`

```python
from windows_use.llms.ollama import ChatOllama

# Requiere Ollama instalado y modelo descargado
llm = ChatOllama(
    model="qwen3-vl:235b-cloud",
    temperature=0.7
)

agent = Agent(llm=llm, browser=Browser.EDGE, use_vision=True)
```

### 6. Otros Proveedores

**Mistral AI:**
```python
from windows_use.llms.mistral import ChatMistral

llm = ChatMistral(
    model="magistral-small-latest",
    api_key="YOUR_MISTRAL_API_KEY",
    temperature=0.7
)
```

**Groq:**
```python
from windows_use.llms.groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key="YOUR_GROQ_API_KEY",
    temperature=0.7
)
```

**Cerebras:**
```python
from windows_use.llms.cerebras import ChatCerebras

llm = ChatCerebras(
    model="cerebras-model",
    api_key="YOUR_CEREBRAS_API_KEY",
    temperature=0.7
)
```

**OpenRouter:**
```python
from windows_use.llms.open_router import ChatOpenRouter

llm = ChatOpenRouter(
    model="anthropic/claude-3-opus",
    api_key="YOUR_OPENROUTER_API_KEY",
    temperature=0.7
)
```

### Variables de Entorno Recomendadas

Crea un archivo `.env` en el directorio raíz:

```env
# Google
GOOGLE_API_KEY=your_google_api_key

# Anthropic
ANTHROPIC_API_KEY=your_anthropic_api_key

# OpenAI
OPENAI_API_KEY=your_openai_api_key

# Azure OpenAI
AOAI_ENDPOINT=https://your-resource.openai.azure.com/
AOAI_DEPLOYMENT_NAME=your-deployment
AOAI_API_KEY=your_azure_api_key
AOAI_MODEL=gpt-4
AOAI_API_VERSION=2025-01-01-preview

# Otros
MISTRAL_API_KEY=your_mistral_api_key
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key

# Telemetría
ANONYMIZED_TELEMETRY=false
```

**Uso:**
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

### Tabla Comparativa de Proveedores

| Proveedor | Soporte Visión | Modelos Locales | Costo Aproximado |
|-----------|----------------|-----------------|------------------|
| Google Gemini | ✅ | ❌ | Medio |
| Anthropic Claude | ✅ | ❌ | Alto |
| OpenAI | ✅ | ❌ | Alto |
| Azure OpenAI | ✅ | ❌ | Alto |
| Ollama | ✅* | ✅ | Gratis |
| Mistral AI | ✅ | ❌ | Medio |
| Groq | ❌ | ❌ | Bajo |
| Cerebras | ❌ | ❌ | Medio |
| OpenRouter | Depende** | ❌ | Variable |

\* Depende del modelo específico  
\** Depende del modelo seleccionado a través de OpenRouter

---

## Sistema de Visión

El sistema de visión permite al agente "ver" capturas de pantalla del escritorio, mejorando significativamente su capacidad para comprender el contexto visual.

### ¿Cómo Funciona?

1. **Captura**: El agente toma una captura del escritorio
2. **Anotación**: Genera cuadros delimitadores y etiquetas sobre elementos interactivos
3. **Envío**: La imagen anotada se envía al LLM junto con el prompt
4. **Interpretación**: El LLM "ve" elementos y sus posiciones exactas
5. **Acción**: El agente puede hacer clic en elementos específicos usando referencias visuales

### Arquitectura del Sistema de Visión

```
┌─────────────────────┐
│  Desktop Screenshot │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  UI Accessibility   │
│       Tree          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Visual Annotation   │
│  (Bounding Boxes    │
│   + Labels)         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Annotated Image     │
│  + Prompt           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Vision-enabled    │
│        LLM          │
└─────────────────────┘
```

### Activar Visión

```python
from windows_use.llms.google import ChatGoogle
from windows_use.agent import Agent, Browser

llm = ChatGoogle(model="gemini-2.5-flash", api_key="YOUR_API_KEY")

# Activar visión con use_vision=True
agent = Agent(
    llm=llm,
    browser=Browser.EDGE,
    use_vision=True  # ← Activar sistema de visión
)
```

### Modelos Compatibles con Visión

✅ **Soportan visión:**
- Google Gemini (todos los modelos 1.5+)
- Anthropic Claude (Claude 3+)
- OpenAI GPT-4 (turbo, vision, 4o)
- Azure OpenAI (GPT-4 con visión)
- Ollama: `llava`, `qwen3-vl`, `minicpm-v`, `bakllava`
- Mistral: `pixtral-12b-2409`, `pixtral-large-latest`

❌ **NO soportan visión:**
- OpenAI GPT-3.5-turbo
- Mayoría de modelos en Groq y Cerebras
- Ollama: `llama3`, `mistral-7b` (solo texto)

### Ventajas del Sistema de Visión

✅ **Mayor Precisión**: El agente puede ver exactamente dónde están los elementos  
✅ **Mejor Comprensión del Contexto**: Entiende el diseño visual de la interfaz  
✅ **Manejo de UI Complejas**: Funciona mejor con interfaces modernas y dinámicas  
✅ **Reducción de Errores**: Menos clics incorrectos en coordenadas equivocadas  

### Desventajas del Sistema de Visión

❌ **Mayor Costo**: Las llamadas con imágenes son más costosas  
❌ **Más Lento**: Procesar imágenes toma más tiempo  
❌ **Uso de Tokens**: Las imágenes consumen muchos tokens  
❌ **Requiere Modelos Específicos**: Solo funciona con modelos que soporten visión  

### Cuándo Usar Visión

**Usa `use_vision=True` cuando:**
- Trabajas con interfaces gráficas complejas
- La precisión visual es crítica
- Los elementos no tienen identificadores claros
- Usas un modelo que soporta visión y el costo no es problema

**Usa `use_vision=False` cuando:**
- Quieres menor costo y mayor velocidad
- La tarea es simple y basada en texto
- Usas un modelo sin soporte de visión
- El árbol de accesibilidad proporciona información suficiente

---

## Opciones de Configuración del Agente

### Constructor Completo

```python
from windows_use.agent import Agent, Browser

agent = Agent(
    llm=llm_instance,                    # Instancia del LLM (requerido)
    instructions=[],                     # Instrucciones adicionales
    browser=Browser.EDGE,                # Navegador por defecto
    max_consecutive_failures=3,          # Reintentos ante fallos
    max_steps=25,                        # Máximo de pasos por tarea
    use_vision=False,                    # Activar/desactivar visión
    auto_minimize=False                  # Minimizar consola automáticamente
)
```

### Parámetros Explicados

- **`llm`** (requerido): Instancia del modelo LLM a utilizar
- **`instructions`**: Lista de instrucciones personalizadas adicionales
- **`browser`**: Navegador predeterminado (`EDGE`, `CHROME`, `FIREFOX`, `BRAVE`)
- **`max_consecutive_failures`**: Reintentos cuando el LLM produce respuestas inválidas (por defecto: 3)
- **`max_steps`**: Número máximo de acciones que puede tomar el agente (por defecto: 25)
- **`use_vision`**: Activar sistema de visión (requiere modelo compatible)
- **`auto_minimize`**: Minimizar automáticamente la ventana de consola al ejecutar

### Ejemplo con Instrucciones Personalizadas

```python
instructions = [
    "Siempre verifica dos veces antes de eliminar archivos",
    "Usa Chrome en lugar de Edge cuando sea posible",
    "Guarda el progreso en archivos de memoria cada 3 pasos"
]

agent = Agent(
    llm=llm,
    instructions=instructions,
    browser=Browser.CHROME,
    max_steps=40
)
```

### Configuraciones Típicas

**Configuración Económica (Modelo Local):**
```python
llm = ChatOllama(model="llama3", temperature=0.5)
agent = Agent(
    llm=llm,
    browser=Browser.EDGE,
    use_vision=False,
    max_steps=15
)
```

**Configuración Premium (Máxima Precisión):**
```python
llm = ChatGoogle(model="gemini-2.5-flash", api_key=api_key, temperature=0.7)
agent = Agent(
    llm=llm,
    browser=Browser.CHROME,
    use_vision=True,
    max_steps=50,
    auto_minimize=True,
    max_consecutive_failures=5
)
```

---

## Ejemplos de Uso Avanzado

### Ejemplo 1: Automatización Básica

```python
from windows_use.llms.google import ChatGoogle
from windows_use.agent import Agent, Browser
import os

api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogle(model="gemini-2.5-flash", api_key=api_key)
agent = Agent(llm=llm, browser=Browser.EDGE)

# Tarea simple
agent.print_response(
    query="Abre el Bloc de notas y escribe 'Hola Mundo'"
)
```

### Ejemplo 2: Modo Interactivo

```python
from windows_use.llms.ollama import ChatOllama
from windows_use.agent import Agent, Browser

# Modelo local para privacidad
llm = ChatOllama(model="qwen3-vl:235b-cloud")
agent = Agent(llm=llm, browser=Browser.EDGE, use_vision=True)

print("🤖 Agente Windows-Use Iniciado")
print("Escribe 'salir' para terminar\n")

while True:
    query = input("👤 Tu consulta: ")
    
    if query.lower() in ['salir', 'exit', 'quit']:
        print("👋 ¡Hasta luego!")
        break
    
    if query.strip():
        agent.print_response(query=query)
        print("\n" + "="*50 + "\n")
```

### Ejemplo 3: Tarea Compleja con Memoria

```python
from windows_use.llms.anthropic import ChatAnthropic
from windows_use.agent import Agent, Browser
import os

api_key = os.getenv("ANTHROPIC_API_KEY")
llm = ChatAnthropic(model="claude-sonnet-4-5", api_key=api_key)

agent = Agent(
    llm=llm,
    browser=Browser.EDGE,
    use_vision=False,
    max_steps=40
)

query = """
Realiza las siguientes tareas:
1. Crea un archivo de memoria llamado 'plan.md' con los pasos a seguir
2. Abre el Explorador de archivos
3. Navega al escritorio
4. Crea una nueva carpeta llamada 'Proyecto'
5. Actualiza el archivo de memoria con el progreso
6. Al finalizar, lee el archivo de memoria y genera un resumen
"""

agent.print_response(query=query)
```

### Ejemplo 4: Análisis del Sistema

```python
from windows_use.llms.google import ChatGoogle
from windows_use.agent import Agent, Browser
import os

api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogle(model="gemini-2.5-flash", api_key=api_key)

agent = Agent(
    llm=llm,
    browser=Browser.EDGE,
    max_steps=30
)

query = """
Analiza el sistema y crea un informe:
1. Ejecuta 'Get-ComputerInfo' para información del sistema
2. Ejecuta 'Get-Process | Sort-Object CPU -Descending | Select-Object -First 10'
3. Ejecuta 'Get-PSDrive' para estado de discos
4. Crea un archivo de memoria con toda esta información organizada
5. Genera un resumen con recomendaciones
"""

agent.print_response(query=query)
```

### Ejemplo 5: Manejo de Errores

```python
from windows_use.llms.google import ChatGoogle
from windows_use.agent import Agent, Browser
import os

api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogle(model="gemini-2.5-flash", api_key=api_key)

agent = Agent(
    llm=llm,
    browser=Browser.EDGE,
    max_steps=20,
    max_consecutive_failures=3
)

def ejecutar_con_manejo_errores(query: str):
    try:
        result = agent.invoke(query)
        
        if result.is_done:
            print(f"✅ Tarea completada exitosamente")
            print(f"📝 Respuesta: {result.output}")
        else:
            print(f"❌ Tarea no completada")
            if result.error:
                print(f"🚨 Error: {result.error}")
        
        print(f"📊 Pasos utilizados: {result.steps}")
        
        return result
        
    except Exception as e:
        print(f"💥 Error inesperado: {str(e)}")
        return None

# Uso
query = "Abre el Bloc de notas y escribe 'Hola Mundo'"
result = ejecutar_con_manejo_errores(query)
```

---

## Solución de Problemas

### Problemas Comunes

#### 1. El agente no puede hacer clic en elementos

**Síntomas:**
- Errores de "elemento no encontrado"
- Clics en coordenadas incorrectas

**Soluciones:**
```python
# Solución 1: Activar visión para mejor precisión
agent = Agent(llm=llm, use_vision=True)

# Solución 2: Usar Wait Tool para dar tiempo a cargar
query = "Abre Chrome, espera 3 segundos, y luego busca Python"

# Solución 3: Aumentar pasos máximos
agent = Agent(llm=llm, max_steps=40)
```

#### 2. El LLM produce respuestas inválidas

**Síntomas:**
- Errores de "formato de respuesta inválido"
- El agente se detiene prematuramente

**Soluciones:**
```python
# Solución 1: Aumentar reintentos
agent = Agent(llm=llm, max_consecutive_failures=5)

# Solución 2: Reducir temperatura para respuestas más precisas
llm = ChatGoogle(model="gemini-2.5-flash", api_key=api_key, temperature=0.5)

# Solución 3: Usar modelo más potente
llm = ChatAnthropic(model="claude-sonnet-4-5", api_key=api_key)
```

#### 3. Problemas de timeout

**Síntomas:**
- Timeout en llamadas al LLM
- Errores de límite de tokens excedido

**Soluciones:**
```python
# Solución 1: Dividir tarea en pasos más pequeños
query1 = "Abre Chrome"
agent.print_response(query=query1)

query2 = "Busca Python documentation"
agent.print_response(query=query2)

# Solución 2: Aumentar max_tokens
llm = ChatAnthropic(model="claude-sonnet-4-5", api_key=api_key, max_tokens=16000)

# Solución 3: Desactivar visión para reducir tokens
agent = Agent(llm=llm, use_vision=False)
```

#### 4. El agente repite las mismas acciones

**Síntomas:**
- Bucles infinitos
- Acciones repetitivas sin progreso

**Soluciones:**
```python
# Solución 1: Reducir max_steps para evitar bucles
agent = Agent(llm=llm, max_steps=15)

# Solución 2: Añadir instrucciones específicas
instructions = [
    "Si una acción falla 2 veces, intenta un enfoque diferente",
    "Usa Memory Tool para rastrear acciones completadas"
]
agent = Agent(llm=llm, instructions=instructions)

# Solución 3: Usar modelo con mejor razonamiento
llm = ChatAnthropic(model="claude-sonnet-4-5", api_key=api_key)
```

#### 5. Problemas con el sistema de visión

**Síntomas:**
- Errores al enviar imágenes
- "Model does not support images"

**Soluciones:**
```python
# Solución 1: Verificar que el modelo soporte visión
# Modelos compatibles:
llm = ChatGoogle(model="gemini-2.5-flash", api_key=api_key)  # ✅
# llm = ChatOllama(model="llama3")  # ❌ (sin visión)

# Solución 2: Usar modelo local con visión
llm = ChatOllama(model="qwen3-vl:235b-cloud")  # ✅

# Solución 3: Desactivar visión
agent = Agent(llm=llm, use_vision=False)
```

### Debugging Avanzado

```python
import logging

# Configurar logging detallado
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(name)s: %(message)s'
)

# Ahora el agente mostrará información detallada
agent = Agent(llm=llm, use_vision=False)
agent.print_response(query="Abre Notepad")
```

### Inspeccionar Resultado del Agente

```python
from windows_use.agent.views import AgentResult

result = agent.invoke(query="Abre Notepad")

print(f"Completado: {result.is_done}")
print(f"Pasos usados: {result.steps}")
print(f"Error: {result.error}")
print(f"Salida: {result.output}")
```

### Mejores Prácticas de Seguridad

⚠️ **IMPORTANTE**: Siempre ejecuta Windows-Use en un entorno aislado:

- ✅ Usar Máquina Virtual (VirtualBox, VMware, Hyper-V)
- ✅ Usar Windows Sandbox (Windows 10/11 Pro/Enterprise)
- ✅ Usar máquina de prueba dedicada
- ❌ NO ejecutar en máquina de producción
- ❌ NO ejecutar con privilegios administrativos innecesarios

Consulta [SECURITY.md](SECURITY.md) para políticas de seguridad completas.

---

## Recursos Adicionales

### Enlaces Útiles

- **Repositorio GitHub**: [https://github.com/CursorTouch/Windows-Use](https://github.com/CursorTouch/Windows-Use)
- **Documentación de Agentes**: [AGENTS.md](AGENTS.md)
- **Política de Seguridad**: [SECURITY.md](SECURITY.md)
- **Guía de Contribución**: [CONTRIBUTING.md](CONTRIBUTING.md)

### Comunidad y Soporte

- **Discord**: [Únete a la comunidad](https://discord.com/invite/Aue9Yj2VzS)
- **Twitter/X**: [@CursorTouch](https://x.com/CursorTouch)
- **Issues**: [Reportar problemas](https://github.com/CursorTouch/Windows-Use/issues)

### Telemetría

Puedes desactivar la telemetría anónima:

```env
# En archivo .env
ANONYMIZED_TELEMETRY=false
```

```python
# En código Python
import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"
```

---

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

---

## Autor

Creado con ❤️ por [Jeomon George](https://github.com/Jeomon)

---

## Citación

```bibtex
@software{
  author       = {George, Jeomon},
  title        = {Windows-Use: Enable AI to control Windows OS},
  year         = {2025},
  publisher    = {GitHub},
  url          = {https://github.com/CursorTouch/Windows-Use}
}
```

---

<div align="center">

**¿Tienes preguntas? [Abre un issue](https://github.com/CursorTouch/Windows-Use/issues) o [únete a Discord](https://discord.com/invite/Aue9Yj2VzS)**

</div>
