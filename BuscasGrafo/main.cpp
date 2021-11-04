#include <iostream>
#include "BuscasGrafo.hpp"

using namespace std;

int main(void) {
    int maximoVertices;
    /* 
    cout << "Maximo vertices: ";
    cin >> maximoVertices; */
    Grafo grafo(6);

    int opcao;

    grafo.insereVertice("Cliente0", 10);
    grafo.insereVertice("Cliente1", 20);
    grafo.insereVertice("Cliente2", 30);
    grafo.insereVertice("Cliente3", 40);
    grafo.insereVertice("Cliente4", 50);
    grafo.insereVertice("Cliente5", 60);

    grafo.insereAresta("Cliente0", "Cliente1", 10);
    grafo.insereAresta("Cliente0", "Cliente2", 20);
    grafo.insereAresta("Cliente1", "Cliente4", 10);
    grafo.insereAresta("Cliente2", "Cliente3", 20);
    grafo.insereAresta("Cliente2", "Cliente4", 33);
    grafo.insereAresta("Cliente1", "Cliente3", 50);
    grafo.insereAresta("Cliente3", "Cliente4", 20);
    grafo.insereAresta("Cliente4", "Cliente5", 1);
    grafo.insereAresta("Cliente3", "Cliente5", 2);

    grafo.imprimirListaAdjacencias();
    Vertice v1 = grafo.buscaVertice("Cliente0");
    Vertice v2 = grafo.buscaVertice("Cliente5");
    grafo.buscaProfundidade(v1, v2);
    grafo.buscaLargura(v1, v2);
    
    /* do
    {
        int peso; 
        double preco;
        string nome, origem, destino;

        cout << "1. Add vertice" << endl;
        cout << "2. Add aresta" << endl;
        cout << "3. Print vertices" << endl;
        cout << "4. Print lista de adjacencias" << endl;
        cin >> opcao;

        switch (opcao) {
            case 0:
                break;
            case 1:
            cout << "Nome: ";
            cin >> nome;

            cout << "Preco: ";
            cin >> preco;

            if(grafo.insereVertice(nome, preco)) 
                cout << "Vertice inserido!" << endl;
            else
                cout << "Vertice NAO inserido!" << endl;
            break;
            case 2:
            cout << "Origem: ";
            cin >> origem;

            cout << "Destino: ";
            cin >> destino;

            cout << "Peso: ";
            cin >> peso;
            if(grafo.insereAresta(origem, destino, peso))
                cout << "Aresta inserida" << endl;
            else
                cout << "Aresta NAO inserida" << endl;
            break;
            case 3:
            grafo.imprimirVertices();
            break;
            case 4:
            grafo.imprimirListaAdjacencias();
            break;
        default:
            break;
        }
    } while (opcao != 0); */
    
    return 0;
}
