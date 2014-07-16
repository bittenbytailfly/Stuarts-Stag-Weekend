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

})

.controller('selectCharacterCtrl', function ($scope, $http, $location, $modal, $timeout) {

    $timeout(function() {
        $http.post('/ajax/characters', { 'characterType': $scope.characterType })
        .success(function (data) {
            console.log(data);
            $scope.characters = data;
        });
    });

    $scope.preview = function (character) {
        var modalInstance = $modal.open({
            templateUrl: '/templates/preview.html',
            controller: 'previewCtrl',
            size: 'lg',
            resolve: {
                character: function () {
                    return character;
                }
            }
        });
    };
})

.controller('previewCtrl', function ($scope, $modalInstance, $http, character) {

    $scope.character = character;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.confirm = function () {
        $http.post('/ajax/select', { 'characterKey': $scope.character.url_safe_key })
        .success(function (data) {
            console.log(data);
            $scope.characters = data;
        });
    };

})

.controller('secretIdentitiesController', function($scope, $http) {

    $http.post('/ajax/get-identities')
        .success(function (data) {
            $scope.identites = data;
        });
});