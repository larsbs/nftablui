import Ember from 'ember';

export default Ember.Route.extend({
  model: function () {
    return this.store.findAll('table');
  },
  setupController: function (controller, model) {
    controller.set('tables', model);
  }
});
