// Data model para cada opcion
const CONFIG = {
    // 1. Mat. Modular
    modulo: { t: "Operación Módulo (A mod N)", d: "Se saca el residuo. Divides el número A entre el límite N, y el sobrante exacto es el Resultado.", bg: "matematica", in: ["a", "n"] },
    inv_aditivo: { t: "Inverso Aditivo", d: "Encontrar un número faltante. ¿Cuánto le falta a 'A' para que la suma pueda dividirse exactamente por 'N' y sobrar 0?", bg: "matematica", in: ["a", "n"] },
    xor: { t: "Operación XOR Binario", d: "Compara bits de 'A' y 'B'. Si los bits son iguales da 0 (Falso), si son distintos da 1 (Verdadero).", bg: "matematica", in: ["a", "b"] },
    mcd: { t: "Máximo Común Divisor (MCD)", d: "Encuentra el número máximo que puede dividir a 'A' y a 'B' sin dejar decimales.", bg: "matematica", in: ["a", "b"] },
    inv_tradicional: { t: "Inverso Multipl. Tradicional", d: "Fuerza Bruta. Multiplica 'A' por todos los números del 1 a 'N' buscando que (A * n) Dividido N sobre 1.", bg: "matematica", in: ["a", "n"] },
    aee: { t: "Algoritmo Extendido (AEE)", d: "Versión rápida matemática. Usa divisiones sucesivas estilo Euclides para encontrar el Inverso sin probar todos los números.", bg: "matematica", in: ["a", "n"] },
    
    // 2. Clasica
    mod27: { t: "Mapeo Módulo 27", d: "Convierte letras en números (A=0, B=1, ... Z=26) que luego usamos para calcular, ignorando mayúsculas y espacios.", bg: "clasica", in: ["texto"] },
    cesar: { t: "Cifrado César", d: "Sustitución. Corre cada letra de tu mensaje ciertas posiciones hacia la derecha (indicado por K).", bg: "clasica", in: ["texto", "clave_num"] },
    vernam: { t: "Cifrado Vernam (Aditivo)", d: "Seguridad inquebrantable. Suma el número de la Letra de tu Mensaje con el número de la Letra de la Clave.", bg: "clasica", in: ["texto", "clave_txt"] },
    atbash: { t: "Cifrado ATBASH", d: "Efecto espejo. Cambia la primera letra por la última (A -> Z, B -> Y).", bg: "clasica", in: ["texto"] },
    columnar: { t: "Transposición Columnar", d: "Reordenar. Mete el texto en una tabla por filas horizontales y luego envía el mensaje leyendo de arriba hacia abajo.", bg: "clasica", in: ["texto", "clave_num"] },
    afin: { t: "Cifrado Afín", d: "Ecuación matemática. Cifra con la función: Cifra = (Letra * A + B) dividido el abc (27).", bg: "clasica", in: ["texto", "a", "b"] },
    sustitucion: { t: "Sustitución Pura", d: "Cambia tu alfabeto de A-Z por otro alfabeto totalmente desordenado que pases como llave.", bg: "clasica", in: ["texto", "clave_txt"] },

    // 3. Moderna
    dh: { t: "Log. Discreto / Diffie-Hellman", d: "Generar clave remota. Eleva una 'Base' pública al exponente de tu 'Secreto Privado', y sácales el Módulo 'P'.", bg: "moderna", in: ["base", "a", "mod"] },
    rsa: { t: "Simulación Sistema RSA", d: "Criptografía asimétrica reina. A partir de 2 números primos y un exponente, construye llaves y cifra el mensaje.", bg: "moderna", in: ["p", "q", "e", "a"] },
    exp_rapida: { t: "Exp. Modular Rápida", d: "Eficiencia pura. En vez de exponenciar un número gigante, lo convierte a binario y aplica módulos intermedios saltando la carga.", bg: "moderna", in: ["base", "exp", "mod"] },

    // 4. Hash
    md5: { t: "Función Hash MD5", d: "Crea una 'huella dactilar' única de 32 letras/números a partir de cualquier texto. Es irreversible pero ya fue rota.", bg: "hash", in: ["texto"] },
    sha256: { t: "Hash Seguro SHA-256", d: "La huella dactilar usada por Bitcoin. Devuelve un texto hexadecimal super-seguro de 64 caracteres.", bg: "hash", in: ["texto"] },
    sha512: { t: "Hash NSA SHA-512", d: "Genera el doble de barrera que SHA-256 (128 caracteres). Usado para sistemas clasificados e hiperseguridad.", bg: "hash", in: ["texto"] },

    // 5. Codificacion
    ascii: { t: "Codificación Máquina ASCII", d: "Muestra cómo la computadora lee las letras. Devuelve números enteros del 0-255 subyacentes.", bg: "codificacion", in: ["texto"] },
    hexa: { t: "Voltaje Hexadecimal", d: "Condensa los Bytes (ceros y unos) en una notación visual base-16 de color Hexadecimal (0 a F).", bg: "codificacion", in: ["texto"] },
    binario: { t: "Datos RAW en Binario", d: "Muestra los 8 bits reales eléctricos (0s y 1s) encendidos o apagados detrás de la codificación.", bg: "codificacion", in: ["texto"] },
    base64: { t: "Base64 URIs", d: "Convierte cualquier archivo o texto informático a 64 caracteres imprimibles en la web (ideal para URLs o emails).", bg: "codificacion", in: ["texto"] },

    // 6. Salt
    md5_salt: { t: "MD5 + Veneno SALT", op:"md5", bg: "salt", d:"Ruido protector. Suma la frase SALT y el Mensaje juntos, y luego les saca la Huella Dactilar para evadir Hackers.", in:["salt", "texto"] },
    sha256_salt: { t: "SHA-256 + Blindaje SALT", op: "sha256", bg: "salt", d:"Pega físicamente el valor SECRET_SALT a tu clave y genera el Hash 256. Intocable.", in:["salt", "texto"] },
    sha512_salt: { t: "SHA-512 + Blindaje SALT", op:"sha512", bg: "salt", d:"Máximo nivel. El mensaje engorda combinando el Salt en bruto antes de aplicar criptografía SHA-512.", in:["salt", "texto"] },
};

const TEMPLATES = {
    "a": { label: "Input numérico [ A ]", type: "number", pl: "Ej: 17" },
    "b": { label: "Input numérico [ B ]", type: "number", pl: "Ej: 5" },
    "n": { label: "Módulo Limitador [ N ]", type: "number", pl: "Ej: 27" },
    "texto": { label: "Data Stream [ T ]", type: "text", pl: "Escribe tu input..." },
    "clave_num": { label: "Valor Cifra [ K ]", type: "number", pl: "Ej: 3" },
    "clave_txt": { label: "Llave de Cifrado [ KEY ]", type: "text", pl: "Ej: SECRETA..." },
    "base": { label: "Gen. Base [ G ]", type: "number", pl: "Ej: 2" },
    "exp": { label: "Exponencial [ EXP ]", type: "number", pl: "Ej: 90" },
    "mod": { label: "Módulo Primo [ P ]", type: "number", pl: "Ej. Primo grande" },
    "p": { label: "Prime [ P ]", type: "number", pl: "Ej: 61" },
    "q": { label: "Prime [ Q ]", type: "number", pl: "Ej: 53" },
    "e": { label: "Public Key Candidate [ E ]", type: "number", pl: "Ej: 17" },
    "salt": { label: "Salt Vector [ SALT ]", type: "text", pl: "Ej: rand_123" },
};

// --- EFECTO SCRAMBLE (DESENCRIPTANDO TEXTO) ---
const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$!%&*+=?/";
async function scrambleText(element, newText, speed = 30) {
    let iteration = 0;
    const oldText = element.innerText;
    const maxIterations = Math.max(newText.length, 10);
    
    return new Promise(resolve => {
        const interval = setInterval(() => {
            element.innerText = newText.split("").map((letter, index) => {
                if(index < iteration) { return newText[index]; }
                return chars[Math.floor(Math.random() * chars.length)];
            }).join("");
            
            if(iteration >= newText.length) {
                clearInterval(interval);
                element.innerText = newText;
                resolve();
            }
            iteration += 1 / 2;
        }, speed);
    });
}

// --- TIPO MÁQUINA DE ESCRIBIR EN TERMINAL ---
async function typeWriter(element, text, speed = 10) {
    element.textContent = "";
    return new Promise(resolve => {
        let i = 0;
        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            } else {
                resolve();
            }
        }
        type();
    });
}

// --- UI EVENT LISTENERS ---
const accordions = document.querySelectorAll('.accordion-item');
const menuItems = document.querySelectorAll('.menu-item');
const tabContent = document.getElementById('tab-content');
let activeOpKey = "";

accordions.forEach(acc => {
    acc.querySelector('.accordion-btn').addEventListener('click', () => {
        accordions.forEach(other => { if (other !== acc) other.classList.remove('active'); });
        acc.classList.toggle('active');
    });
});

menuItems.forEach(item => {
    item.addEventListener('click', () => {
        menuItems.forEach(i => i.classList.remove('active'));
        item.classList.add('active');
        accordions.forEach(acc => acc.classList.remove('active'));
        
        const mainMenu = document.getElementById('main-menu');
        if(mainMenu) mainMenu.classList.remove('open');
        
        let opValue = item.getAttribute('data-op');
        let bgKey = item.getAttribute('data-api');
        if(bgKey === "salt") { opValue += "_salt"; }
        activeOpKey = opValue;
        
        renderForm();
    });
});

document.addEventListener('click', (e) => {
    if (!e.target.closest('.accordion-item')) {
        accordions.forEach(acc => acc.classList.remove('active'));
    }
});

async function renderForm() {
    const data = CONFIG[activeOpKey];
    
    // Aplicamos Scramble solo al título, la descripción va directa
    const titleEl = document.getElementById('header-title');
    const descEl = document.getElementById('header-desc');
    
    scrambleText(titleEl, data.t, 20);
    descEl.textContent = data.d;
    
    document.getElementById('result-container').style.display = 'none';

    let html = "";
    data.in.forEach(field => {
        let tmpl = TEMPLATES[field];
        html += `
        <div class="input-group">
            <label for="inp_${field}">${tmpl.label}</label>
            <div class="input-wrapper">
                <input type="${tmpl.type}" id="inp_${field}" placeholder="${tmpl.pl}" autocomplete="off">
            </div>
        </div>`;
    });
    
    html += `<button class="btn-primary" onclick="ejecutarCalculo()">[ INICIAR ALGORITMO ]</button>`;
    tabContent.innerHTML = html;
}

// --- FETCH AL BACKEND ---
async function ejecutarCalculo() {
    const btn = document.querySelector('.btn-primary');
    const prevText = btn.textContent;
    await scrambleText(btn, "ESTABLECIENDO CONEXIÓN...", 20);
    btn.disabled = true;
    
    const data = CONFIG[activeOpKey];
    let originalOp = activeOpKey;
    if(originalOp.includes("_salt")) originalOp = originalOp.replace("_salt", "");

    const payload = { op: originalOp, category: data.bg };
    
    data.in.forEach(field => {
        let el = document.getElementById('inp_' + field);
        if(TEMPLATES[field].type === "number") {
            payload[field] = parseInt(el.value) || 0;
        } else {
            payload[field] = el.value || "";
        }
    });

    try {
        const bgPath = "/api";
        const resp = await fetch(bgPath, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        const json = await resp.json();
        
        document.getElementById('result-container').style.display = 'block';
        const outputEl = document.getElementById('output-text');
        
        // Efecto Typewriter para la salida del backend
        await typeWriter(outputEl, json.resultado || "Aviso: Respuesta nula del servidor.", 5);
        
    } catch(err) {
        document.getElementById('result-container').style.display = 'block';
        const outputEl = document.getElementById('output-text');
        await typeWriter(outputEl, `[!] ANOMALÍA SISTEMA: Error conectando con núcleo backend.\nDetalle: ${err.message}`, 10);
    } finally {
        await scrambleText(btn, prevText, 20);
        btn.disabled = false;
    }
}

// Menú Hamburguesa
const hamburgerBtn = document.getElementById('hamburger-btn');
const mainMenu = document.getElementById('main-menu');
if (hamburgerBtn && mainMenu) {
    hamburgerBtn.addEventListener('click', () => {
        mainMenu.classList.toggle('open');
    });
}