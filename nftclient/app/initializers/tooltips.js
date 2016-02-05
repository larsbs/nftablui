import Ember from 'ember';

export default {
    name: "tooltips",
    initialize: function () {
        Ember.$(document).tooltip({
            container: '.navbar',
            delay: { "show": 300, "hide": 50 },
            selector: '[data-toggle="tooltip"]',
            html: true
        });
    }
};
