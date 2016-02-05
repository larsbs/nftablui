import DS from 'ember-data';

export default DS.RESTAdapter.extend({
  namespace: 'api',
  //host: 'http://localhost:8000'

  shouldReloadAll: function () {
    return true;
  },
  shouldBackgroundReloadRecord: function () {
    return false;
  }
});
