/// <reference types="cypress" />

declare namespace Cypress {
    interface Chainable<Subject> {
        /**
         * Run an Management command.
         *
         * @example
         * cy.manage()
         */
        manage(command: string, parameters?: string[]): Chainable<any>;
        /**
         * Get the CSRF Token.
         *
         * @example
         * cy.csrfToken()
         */
        csrfToken(): Chainable<any>;
    }
}