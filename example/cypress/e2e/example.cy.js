describe('Example Test', () => {
    before(() => {
        cy.migrate();
    })

    it('shows a homepage', () => {
        cy.visit('/');

        cy.contains('Django');
    });
});