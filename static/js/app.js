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
            keyboard: false,
            backdrop: 'static',
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

})

.controller('secretIdentitiesController', function($scope, $http, $modal) {

    $http.post('/ajax/get-identities')
        .success(function (data) {
            $scope.secretIdentity = data.secretIdentity;
            $scope.participants = data.participants;
        });

    $scope.change = function() {
        var modalInstance = $modal.open({
            templateUrl: '/templates/confirm-removal.html',
            controller: 'removeIdentityCtrl',
            size: 'lg',
            keyboard: false,
            backdrop: 'static',
            resolve: {
                characterName: function () {
                    return $scope.secretIdentity.character_name;
                }
            }
        });
    };
})

.controller('removeIdentityCtrl', function ($scope, $modalInstance, characterName) {

    $scope.characterName = characterName;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

});