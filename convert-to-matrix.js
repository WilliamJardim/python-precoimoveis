const fs = require('fs');

// Passo 1: Ler o arquivo JSON
const jsonFilePath = './realistic_real_estate_dataset.json';
const txtFilePath = './real_estate_matrix.txt';

fs.readFile(jsonFilePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Erro ao ler o arquivo JSON:', err);
    return;
  }

  try {
    // Passo 2: Converter JSON para matriz
    const jsonData = JSON.parse(data); // Parse do JSON
    const matrix = Object.values(jsonData).map(item => Object.values(item)); // Converter para matriz

    // Criar uma string que pode ser copiada no navegador
    const matrixString = JSON.stringify(matrix);

    // Passo 3: Salvar o conteúdo como um arquivo .txt
    fs.writeFile(txtFilePath, matrixString, 'utf8', err => {
      if (err) {
        console.error('Erro ao salvar o arquivo .txt:', err);
        return;
      }
      console.log(`Matriz salva em: ${txtFilePath}`);
    });
  } catch (parseError) {
    console.error('Erro ao converter JSON para matriz:', parseError);
  }
});
