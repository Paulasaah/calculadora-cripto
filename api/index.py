from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
import hashlib
import math
import base64

app = FastAPI()

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
TAM_ALFABETO = len(ALFABETO)

class CryptoRequest(BaseModel):
    op: Optional[str] = ""
    category: Optional[str] = ""
    texto: Optional[str] = ""
    # Numeros
    base: Optional[int] = 0
    exp: Optional[int] = 0
    mod: Optional[int] = 0
    a: Optional[int] = 0
    b: Optional[int] = 0
    n: Optional[int] = 0
    # Claves
    clave_num: Optional[int] = 0
    clave_txt: Optional[str] = ""
    salt: Optional[str] = ""
    # RSA
    p: Optional[int] = 0
    q: Optional[int] = 0
    e: Optional[int] = 0


# --- UTILIDADES ---
def clean_text(t):
    return "".join(c.upper() for c in str(t) if c.upper() in ALFABETO)

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclides_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def inverso_multiplicativo(a, m):
    gcd, x, _ = euclides_extendido(a, m)
    if gcd != 1:
        return None  # No existe
    return (x % m + m) % m


# --- DISPATCHER ÚNICO PARA VERCEL Y LOCAL ---
@app.post("/api")
async def main_handler(req: CryptoRequest):
    if req.category == "matematica":
        return await handle_matematica(req)
    elif req.category == "clasica":
        return await handle_clasica(req)
    elif req.category == "moderna":
        return await handle_moderna(req)
    elif req.category == "hash":
        return await handle_hash(req)
    elif req.category == "codificacion":
        return await handle_codificacion(req)
    elif req.category == "salt":
        return await handle_salt(req)
    return {"resultado": "Categoría no válida"}


# --- LÓGICA DE NEGOCIO (REFACTORIZADA A FUNCIONES) ---

async def handle_matematica(req: CryptoRequest):
    res = ""
    if req.op == "modulo":
        if req.n == 0: return {"resultado": "Error: n no puede ser 0"}
        r = req.a % req.n
        cociente = req.a // req.n
        res = (f"Procedimiento:\n"
               f"1. Dividir {req.a} / {req.n}\n"
               f"2. Cociente entero = {cociente}\n"
               f"3. Verificando: {req.n} * {cociente} = {req.n * cociente}\n"
               f"4. Residuo = {req.a} - ({req.n * cociente}) = {r}\n\n"
               f"Resultado Final:\n{req.a} mod {req.n} = {r}")
        
    elif req.op == "inv_aditivo":
        if req.n == 0: return {"resultado": "Error: n no puede ser 0"}
        r = (req.n - (req.a % req.n)) % req.n
        res = (f"Procedimiento para Inverso Aditivo de {req.a} mod {req.n}:\n"
               f"Formula: (N - (A mod N)) mod N\n"
               f"1. A mod N = {req.a} mod {req.n} = {req.a % req.n}\n"
               f"2. Restamos al Modulo N: {req.n} - {req.a % req.n} = {req.n - (req.a % req.n)}\n"
               f"3. Aplicar Modulo Final: {req.n - (req.a % req.n)} mod {req.n} = {r}\n\n"
               f"Resultado Final:\nEl Inverso aditivo es {r}")
        
    elif req.op == "xor":
        r = req.a ^ req.b
        len_bin = max(req.a.bit_length(), req.b.bit_length())
        bin_a = format(req.a, f'0{len_bin}b')
        bin_b = format(req.b, f'0{len_bin}b')
        bin_r = format(r, f'0{len_bin}b')
        res = (f"Procedimiento Operación XOR:\n\n"
               f"Número A: {req.a}\n"
               f"Número B: {req.b}\n\n"
               f"Comparación de bits paralela:\n"
               f"   {bin_a} (A)\n"
               f"^  {bin_b} (B)\n"
               f"------------------\n"
               f"=  {bin_r} (Resultado Binario)\n\n"
               f"Resultado Final decimal:\n{req.a} XOR {req.b} = {r}")
        
    elif req.op == "mcd":
        a, b = req.a, req.b
        pasos = f"Procedimiento Algoritmo de Euclides para MCD({a}, {b}):\n\n"
        while b != 0:
            q = a // b
            rem = a % b
            pasos += f"{a} = {b} * {q} + {rem}\n"
            a, b = b, rem
        pasos += f"\nComo el residuo ha llegado a 0, el MCD es {a}.\n"
        if a == 1:
            pasos += "-> Son números COPRIMOS. Comparten inverso multiplicativo directo."
        else:
            pasos += "-> NO SON COPRIMOS. No tienen inverso bidireccional."
        res = pasos
            
    elif req.op == "inv_tradicional":
        if req.n == 0: return {"resultado": "Error: n no puede ser 0"}
        inv = None
        pasos = f"Búsqueda por fuerza bruta de Inverso Multiplicativo de {req.a} mod {req.n}:\nFormula: (A * i) mod N = 1\n\nIteraciones:\n"
        for i in range(1, req.n):
            val = (req.a * i) % req.n
            if i <= 15 or (req.n - i <= 5) or val == 1:
                pasos += f"Iter {i:3}: ({req.a} * {i}) mod {req.n} = {val}"
                if val == 1:
                    pasos += " <--- ¡ÉXITO! Encontramos el 1\n"
                    inv = i
                    break
                else:
                    pasos += "\n"
            elif i == 16:
                pasos += "... (omitiendo pasos intermedios) ...\n"
        if inv is not None:
            res = pasos + f"\nResultado Final:\nInverso de {req.a} mod {req.n} es {inv}"
        else:
            res = pasos + f"\nResultado Final:\nEl inverso NO existe. No hay iteración que dé 1."
            
    elif req.op == "aee":
        if req.n == 0: return {"resultado": "Error: n no puede ser 0"}
        r0, r1 = req.n, req.a % req.n
        s0, s1 = 1, 0
        t0, t1 = 0, 1
        pasos = f"Calculando Inverso de {req.a} mod {req.n}:\n"
        pasos += f"{'q':>5} | {'r0':>5} | {'r1':>5} | {'r':>5} | {'s0':>5} | {'s1':>5} | {'s':>5} | {'t0':>5} | {'t1':>5} | {'t':>5}\n"
        pasos += "-"*75 + "\n"
        while r1 != 0:
            q = r0 // r1
            r = r0 - q * r1
            s = s0 - q * s1
            t = t0 - q * t1
            pasos += f"{q:5} | {r0:5} | {r1:5} | {r:5} | {s0:5} | {s1:5} | {s:5} | {t0:5} | {t1:5} | {t:5}\n"
            r0, r1 = r1, r
            s0, s1 = s1, s
            t0, t1 = t1, t
        if r0 == 1:
            res = pasos + f"\nProcedimiento Exitoso.\nResultado: El inverso de {req.a} mod {req.n} es {(t0 % req.n)}"
        else:
            res = pasos + f"\nFallo Matemático.\nResultado: No existe inverso (El MCD es {r0}, y no 1)."
    return {"resultado": res}

async def handle_clasica(req: CryptoRequest):
    res = ""
    txt = clean_text(req.texto)
    if req.op == "mod27":
        nums = []
        pasos = "Paso a paso de Asignación Módulo 27 (A=0 ... Z=26):\n\n"
        for c in txt:
            idx = ALFABETO.find(c)
            nums.append(str(idx))
            pasos += f"Letra '{c}' -> Índice {idx}\n"
        res = pasos + "\nResultado Final:\n" + " ".join(nums)
    elif req.op == "cesar":
        cifrado = ""
        pasos = f"Paso a paso Cifrado César (K = {req.clave_num}):\nFormula: (Pos + K) mod 27\n\n"
        for c in txt:
            p = ALFABETO.find(c)
            n_p = (p + req.clave_num) % TAM_ALFABETO
            n_c = ALFABETO[n_p]
            pasos += f"'{c}' (Pos: {p:2}) + {req.clave_num} = {(p+req.clave_num):2} mod 27 -> Pos: {n_p:2} -> '{n_c}'\n"
            cifrado += n_c
        res = pasos + f"\nResultado Final:\n{cifrado}"
    elif req.op == "vernam":
        clave = clean_text(req.clave_txt)
        if len(clave) < len(txt):
            veces = math.ceil(len(txt) / max(len(clave), 1))
            clave = (clave * veces)[:len(txt)]
        cifrado = ""
        pasos = f"Paso a paso Cifrado Vernam (Suma paralela mod 27):\nTexto:  {txt}\nClave:  {clave}\n\n"
        pasos += f"{'L_Txt':^7} | {'P_Txt':^7} | {'L_Clv':^7} | {'P_Clv':^7} | {'Suma':^6} | {'Mod27':^6} | {'NuevaL':^7}\n"
        pasos += "-"*65 + "\n"
        for i, c in enumerate(txt):
            p_t = ALFABETO.find(c)
            c_k = clave[i] if i < len(clave) else ALFABETO[0]
            p_k = ALFABETO.find(c_k)
            suma = p_t + p_k
            n_p = suma % TAM_ALFABETO
            n_c = ALFABETO[n_p]
            pasos += f"{c:^7} | {p_t:^7} | {c_k:^7} | {p_k:^7} | {suma:^6} | {n_p:^6} | {n_c:^7}\n"
            cifrado += n_c
        res = pasos + f"\nResultado Final Cifrado:\n{cifrado}"
    elif req.op == "atbash":
        cifrado = ""
        pasos = "Paso a paso Cifrado ATBASH (Espejo Z - Pos):\n\n"
        for c in txt:
            p = ALFABETO.find(c)
            n_p = TAM_ALFABETO - 1 - p
            n_c = ALFABETO[n_p]
            pasos += f"'{c}' (Pos: {p:2}) -> Simétrica (26 - {p:2}) -> Pos: {n_p:2} -> '{n_c}'\n"
            cifrado += n_c
        res = pasos + f"\nResultado Final ATBASH:\n{cifrado}"
    elif req.op == "columnar":
        k = req.clave_num
        if k <= 1: return {"resultado": "La clave columnas (ancho) debe ser mayor a 1."}
        matriz = [txt[i:i+k] for i in range(0, len(txt), k)]
        if len(matriz[-1]) < k:
            matriz[-1] += 'X' * (k - len(matriz[-1]))
        pasos = f"Paso a paso Transposición Columnar (Columnas = {k}):\n\n1. Creando Matriz de inserción por Filas:\n"
        for fila in matriz:
            pasos += "   " + " ".join(list(fila)) + "\n"
        pasos += "\n2. Leyendo de arriba a abajo por Columnas verticales:\n"
        cifrado = ""
        for col in range(k):
            fragmento = ""
            for fila in matriz: fragmento += fila[col]
            pasos += f"   Columna {col + 1}: {fragmento}\n"
            cifrado += fragmento
        res = pasos + f"\nResultado Final Unión Horizontal:\n{cifrado}"
    elif req.op == "afin":
        a, b = req.a, req.b
        if mcd(a, TAM_ALFABETO) != 1:
            return {"resultado": f"Error Matemático: 'a' ({a}) no es COPRIMO con el abecedario (27)."}
        cifrado = ""
        pasos = f"Paso a paso Cifrado Afín:\nFormula: C = (A*P + B) mod 27 -> ({a}*P + {b}) mod 27\n\n"
        for c in txt:
            p = ALFABETO.find(c)
            apb = (a * p) + b
            n_p = apb % TAM_ALFABETO
            n_c = ALFABETO[n_p]
            pasos += f"'{c}' (P={p:2}) -> {a}*{p:2} + {b} = {apb:3} mod 27 -> {n_p:2} -> '{n_c}'\n"
            cifrado += n_c
        res = pasos + f"\nResultado Final:\n{cifrado}"
    elif req.op == "sustitucion":
        clave = clean_text(req.clave_txt)
        if len(set(clave)) != TAM_ALFABETO:
            return {"resultado": "Error: La clave debe contener exactamente 27 letras únicas del abecedario (A-Z + Ñ)."}
        cifrado = ""
        pasos = f"Paso a paso Sustitución Pura:\nAlfabeto Base: {ALFABETO}\nAlfabeto Llave:{clave}\n\n"
        for c in txt:
            idx = ALFABETO.find(c)
            n_c = clave[idx]
            pasos += f"'{c}' (Pos {idx}) === mapea a ===> '{n_c}'\n"
            cifrado += n_c
        res = pasos + f"\nResultado Final Cifrado:\n{cifrado}"
    return {"resultado": res}

async def handle_moderna(req: CryptoRequest):
    res = ""
    if req.op == "dh":
        valor_publico = pow(req.base, req.a, req.mod) 
        res = (f"Procedimiento Diffie-Hellman:\n1. Se escoge secreto x = {req.a}\n2. Y = g^x mod p = {req.base}^{req.a} mod {req.mod}\n\nResultado Final:\n{valor_publico}")
    elif req.op == "rsa":
        n = req.p * req.q
        phi = (req.p - 1) * (req.q - 1)
        if mcd(req.e, phi) != 1: return {"resultado": "Error: e no es coprima con Phi."}
        d = inverso_multiplicativo(req.e, phi)
        cifrado = pow(req.a, req.e, n)
        res = (f"Procedimiento RSA:\nN={n}, Phi={phi}, D={d}\n\nResultado Final (Cipher):\n{cifrado}")
    elif req.op == "exp_rapida":
        bin_exp = bin(req.exp)[2:]
        pasos = f"Exponenciación Rápida ({req.base}^{req.exp} mod {req.mod}):\nBit a bit: "
        r = 1
        for bit in bin_exp:
            r = (r * r) % req.mod
            if bit == '1': r = (r * req.base) % req.mod
        res = pasos + f"\nResultado Final:\n{r}"
    return {"resultado": res}

async def handle_hash(req: CryptoRequest):
    t = req.texto.encode('utf-8')
    h = ""
    pasos = f"Evaluando función Hash unidireccional ({req.op.upper()}):\n\n"
    pasos += f"1. Texto original capturado: '{req.texto}'\n"
    pasos += f"2. Convirtiendo a Bytes UTF-8: {t}\n"
    
    if req.op == "md5": 
        h = hashlib.md5(t).hexdigest()
        pasos += f"3. Procesando algoritmo de Message-Digest de 128 Bits...\n"
    elif req.op == "sha256": 
        h = hashlib.sha256(t).hexdigest()
        pasos += f"3. Procesando NSA Secure Hash Algorithm de 256 Bits...\n"
    elif req.op == "sha512": 
        h = hashlib.sha512(t).hexdigest()
        pasos += f"3. Procesando NSA Secure Hash Algorithm de 512 Bits...\n"
        
    pasos += f"\nResultado Final (Digest):\n{h}"
    return {"resultado": pasos}

async def handle_codificacion(req: CryptoRequest):
    t, b = req.texto, req.texto.encode('utf-8')
    res = ""
    pasos = f"Mapeo y Conversión de Datos ({req.op.upper()}):\n\n"
    pasos += f"1. Texto en bruto: '{t}'\n"
    
    if req.op == "ascii": 
        pasos += "2. Obteniendo los códigos decímales estándares:\n"
        res = " ".join(str(ord(c)) for c in t)
    elif req.op == "hexa": 
        pasos += "2. Pasando el array de Bytes a dígitos hexadecimales (0-F):\n"
        res = b.hex().upper()
    elif req.op == "binario": 
        pasos += "2. Extrayendo los 8-bits por cada carácter:\n"
        res = " ".join(format(x, '08b') for x in b)
    elif req.op == "base64": 
        pasos += "2. Codificación Base64 MIME (6 bits por carácter):\n"
        res = base64.b64encode(b).decode('utf-8')
        
    pasos += f"\nData Final:\n{res}"
    return {"resultado": pasos}

async def handle_salt(req: CryptoRequest):
    combinado = req.salt + req.texto
    b_combinado = combinado.encode('utf-8')
    h = ""
    pasos = f"Blindaje SALT Criptográfico ({req.op.upper()}):\n\n"
    pasos += f"1. Vector SALT original: '{req.salt}'\n"
    pasos += f"2. Mensaje objetivo: '{req.texto}'\n"
    pasos += f"3. Concatenando información sucia (S + M) = '{combinado}'\n"
    pasos += f"4. Aplicando función Hash {req.op.upper()} a la cadena completa...\n"
    
    if req.op == "md5": h = hashlib.md5(b_combinado).hexdigest()
    elif req.op == "sha256": h = hashlib.sha256(b_combinado).hexdigest()
    elif req.op == "sha512": h = hashlib.sha512(b_combinado).hexdigest()
    
    pasos += f"\nToken Dactilar con Inmunidad:\n{h}"
    return {"resultado": pasos}

# Descomentar solo para probar localmente, en Vercel debe estar comentado
# app.mount("/", StaticFiles(directory=".", html=True), name="static")
