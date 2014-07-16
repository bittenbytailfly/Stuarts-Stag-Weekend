'use strict';

angular.module('superheroSelector', ['ui.bootstrap'])

.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('//');
    $interpolateProvider.endSymbol('//');
})

.config(function ($locationProvider) {
    $locationProvider.html5Mode(true);
})

.controller('selectTypeCtrl', function ($scope, $http) {

    $http.post('/ajax/availableTypes')
        .success(function (data) {
            $scope.heroes = data.heroes;
            $scope.villains = data.villains;
        });
})

.controller('selectCharacterCtrl', function ($scope, $http, $location, $modal) {

    (function() {
        var urlSplit = $location.path().split("/");
        $scope.characterType = urlSplit[urlSplit.length - 1];
        $scope.participantKey = urlSplit[urlSplit.length - 2];
        $http.post('/ajax/characters', { 'characterType': $scope.characterType })
        .success(function (data) {
            console.log(data);
            $scope.characters = data;
        });
    }());

    $scope.preview = function (character) {
        var modalInstance = $modal.open({
            templateUrl: '/templates/preview.html',
            controller: 'previewCtrl',
            size: 'lg',
            resolve: {
                character: function () {
                    return character;
                },
                participantKey: function () {
                    return $scope.participantKey
                }
            }
        });
    };
})

.controller('previewCtrl', function ($scope, $modalInstance, $http, character, participantKey) {

    $scope.character = character;
    $scope.participantKey = participantKey;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.confirm = function () {
        $http.post('/ajax/select', { 'participantKey': $scope.participantKey, 'characterKey': $scope.character.url_safe_key })
        .success(function (data) {
            console.log(data);
            $scope.characters = data;
        });
    };

})

.controller('secretIdentitiesController', function($scope) {
    
    $http.post('/ajax/get-identities')
        .success(function (data) {
            $scope.identites = data;
        });
    
});