describe('Test API Users', () => {
    it('should fetch all users', () => {
        cy.request('GET', '/api/users')
            .its('status')
            .should('equal', 200);
    });

    it('should create a new user', () => {
        const user = {
            firstname: "Test",
            lastname: "Dutest",
            email: "test@gmail.com",
            password: "monpass",
            birthdate: "2000-01-01",
            city: "Nice",
            postal_code: "06200"
        };

        cy.request('POST', '/api/users', user)
            .its('status')
            .should('equal', 201);
    });
});
  