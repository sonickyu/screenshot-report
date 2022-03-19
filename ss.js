const puppeteer = require("puppeteer");

(async () => {
 // Criar uma instância para um browser
 const browser = await puppeteer.launch({
  headless: true, defaultViewport: {width: 1024, height: 1024}, // headless: true or false; defaultViewport screen resolution.
  args: ["--no-sandbox","--start-maximized"],

});

// literalmente a página
const page = await browser.newPage();
await page.setExtraHTTPHeaders({
        'Accept-Language': 'pt-BR' // Tradução da página
    });

// Acessa qualquer página inserida no campo page.goto("URL DA PÁGINA").
await page.goto("URL DA PÁGINA AQUI", { waitUntil: "networkidle0" });
await page.waitFor(7500); // espera 7 segundos e meio para a próxma linha 

await page.click(`input[name="user"]`); // Da um click falso no input de login (deve prourar o input e alterar o campo name="user")
await page.keyboard.type("Insira o usuário aqui"); // digita uma string no input
await page.click('input[type="password"]'); //Da um click falso no input de sennha
await page.keyboard.type("Insira a senha aqui"); // digita uma string no input (deve procurar o input e alterar o campo type="password")
await page.keyboard.press('Enter'); // Tecla Enter para confirmar o Login

await page.waitFor(10000); // espera 10 segundos para a próxma linha 
await page.screenshot({
  path: '/home/ubuntu/email/ss.png', // Image Dimensions : 1920 x 1080, Tira Screenshot e salva como .png
});

browser.close();

})();
