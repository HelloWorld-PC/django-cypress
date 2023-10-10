describe('Example Test', () => {
    before(() => {
        // either run cy.migrate() or cy.refreshDatabase().
        // it depends on your case
        cy.migrate(); 
        cy.refreshDatabase();
    })

    it('shows a homepage', () => {
        cy.visit('/');

        cy.contains('Django');
    });
});