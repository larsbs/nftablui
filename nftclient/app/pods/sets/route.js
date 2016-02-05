import Ember from 'ember';

export default Ember.Route.extend({
  model: function () {
    return this.store.findAll('set');
  },
  setupController: function (controller, model) {
    controller.set('sets', model);
  }
});
