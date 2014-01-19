var myObject = {
  status: false,
  speed: 0
}

App = Ember.Application.create();

App.Router.map(function() {
  this.route("users");
  this.route("countries");
});

DS.RESTAdapter.configure("plurals", {
  country: "countries"
});

App.Store = DS.Store.extend({
  revision: 12,
  adapter: DS.RESTAdapter.extend({
    serializer: DS.RESTSerializer.extend({
      primaryKey: function (type) {
        return '_id';
      }
    })
  })
});

App.User = DS.Model.extend({
  name: DS.attr('string')
});

App.Country = DS.Model.extend({
  name: DS.attr('string')
});

App.UsersRoute = Ember.Route.extend({
  model: function() {
    return App.User.find();
  }
});

App.CountriesRoute = Ember.Route.extend({
  model: function() {
    return App.Country.find();
  }
});

App.LoadingRoute = Ember.Route.extend();
