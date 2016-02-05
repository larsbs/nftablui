import Ember from 'ember';

export default Ember.Route.extend({
  model: function (params) {
    return this.store.findRecord('chain', params.chain_id);
  },
  setupController: function (controller, model) {
    controller.set('chain', model);
  }
});
