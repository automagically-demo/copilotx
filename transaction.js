async function getTaxRate(zipCode) {
    // This function would make an AJAX call to your server-side script
    // For the purpose of this example, we'll just return a fixed tax rate
    return 0.07;  // 7% tax rate
}

async function calculateTax(zipCode, amount) {
    const taxRate = await getTaxRate(zipCode);
    return amount * taxRate;
}

// Usage
calculateTax('90210', 100).then(tax => console.log(`Tax: $${tax.toFixed(2)}`));