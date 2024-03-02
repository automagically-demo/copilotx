const taxRatesByZipCode = {
    '10001': 0.08, // New York
    '94101': 0.085, // San Francisco
    // Add more zip codes and tax rates as needed
};

function calculateTax(amount, zipCode) {
    const taxRate = taxRatesByZipCode[zipCode];
    if (taxRate === undefined) {
        throw new Error(`No tax rate found for zip code ${zipCode}`);
    }
    return amount * taxRate;
}