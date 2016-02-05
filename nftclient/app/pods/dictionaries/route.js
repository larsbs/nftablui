import Ember from 'ember';

export default Ember.Route.extend({
  model: function () {
    return this.store.findAll('dictionary');
  },
  setupController: function (controller, model) {
    controller.set('dictionaries', model);
  }
});
